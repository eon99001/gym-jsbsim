from types import MethodType
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext
from distutils.extension import Extension
from distutils.util import get_platform
import sys

with open('README.md') as f:
    long_description = f.read()

libraries = []
if get_platform() == 'mingw':
    libraries = ['ws2_32']

extra_compile_args = ['-DHAVE_EXPAT_CONFIG_H']
if sys.platform == 'win32':
    extra_compile_args.append('-DJSBSIM_VERSION=\\"1.0.0.dev1\\"')
else:
    extra_compile_args.append('-DJSBSIM_VERSION=\"1.0.0.dev1\"')


def new_compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
    if src[-1] != 'c' and '-std=c++11' not in extra_postargs:
        extra_postargs.append('-std=c++11')
    if src[-1] == 'c' and '-std=c++11' in extra_postargs:
        extra_postargs.remove('-std=c++11')
    self.old_compile(obj, src, ext, cc_args, extra_postargs, pp_opts)


class custom_build_ext(build_ext):
    def build_extension(self, ext):
        self.compiler.old_compile = self.compiler._compile
        self.compiler._compile = MethodType(new_compile, self.compiler)
        super().build_extension(ext)


setup(
    name='gym_jsbsim',
    version='0.1.0',
    url='https://github.com/galleon/gym-jsbsim/tree/new/gym_jsbsim',
    author='Guillaume Alleon',
    author_email='guillaume.alleon@gmail.com',
    license='LGPL 2.1',
    description='Gym JSBSim environment',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    cmdclass={'build_ext': custom_build_ext},
    ext_modules=[Extension('jsbsim', ['gym_jsbsim/jsbsim/python/jsbsim.pyx', 'gym_jsbsim/jsbsim/src/FGFDMExec.cpp','gym_jsbsim/jsbsim/src/FGJSBBase.cpp','gym_jsbsim/jsbsim/src/initialization/FGInitialCondition.cpp','gym_jsbsim/jsbsim/src/initialization/FGTrim.cpp','gym_jsbsim/jsbsim/src/initialization/FGTrimAxis.cpp','gym_jsbsim/jsbsim/src/models/atmosphere/FGMSIS.cpp','gym_jsbsim/jsbsim/src/models/atmosphere/FGMSISData.cpp','gym_jsbsim/jsbsim/src/models/atmosphere/FGMars.cpp','gym_jsbsim/jsbsim/src/models/atmosphere/FGStandardAtmosphere.cpp','gym_jsbsim/jsbsim/src/models/atmosphere/FGWinds.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGDeadBand.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGFCSComponent.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGFilter.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGGain.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGKinemat.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGSummer.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGSwitch.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGFCSFunction.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGSensor.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGPID.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGActuator.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGAccelerometer.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGGyro.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGLinearActuator.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGMagnetometer.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGAngles.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGWaypoint.cpp','gym_jsbsim/jsbsim/src/models/flight_control/FGDistributor.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGElectric.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGEngine.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGForce.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGNozzle.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGPiston.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGPropeller.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGRocket.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGTank.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGThruster.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGTurbine.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGTurboProp.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGTransmission.cpp','gym_jsbsim/jsbsim/src/models/propulsion/FGRotor.cpp','gym_jsbsim/jsbsim/src/models/FGAerodynamics.cpp','gym_jsbsim/jsbsim/src/models/FGAircraft.cpp','gym_jsbsim/jsbsim/src/models/FGAtmosphere.cpp','gym_jsbsim/jsbsim/src/models/FGAuxiliary.cpp','gym_jsbsim/jsbsim/src/models/FGFCS.cpp','gym_jsbsim/jsbsim/src/models/FGSurface.cpp','gym_jsbsim/jsbsim/src/models/FGGroundReactions.cpp','gym_jsbsim/jsbsim/src/models/FGInertial.cpp','gym_jsbsim/jsbsim/src/models/FGLGear.cpp','gym_jsbsim/jsbsim/src/models/FGMassBalance.cpp','gym_jsbsim/jsbsim/src/models/FGModel.cpp','gym_jsbsim/jsbsim/src/models/FGOutput.cpp','gym_jsbsim/jsbsim/src/models/FGPropagate.cpp','gym_jsbsim/jsbsim/src/models/FGPropulsion.cpp','gym_jsbsim/jsbsim/src/models/FGInput.cpp','gym_jsbsim/jsbsim/src/models/FGExternalReactions.cpp','gym_jsbsim/jsbsim/src/models/FGExternalForce.cpp','gym_jsbsim/jsbsim/src/models/FGBuoyantForces.cpp','gym_jsbsim/jsbsim/src/models/FGGasCell.cpp','gym_jsbsim/jsbsim/src/models/FGAccelerations.cpp','gym_jsbsim/jsbsim/src/math/FGColumnVector3.cpp','gym_jsbsim/jsbsim/src/math/FGFunction.cpp','gym_jsbsim/jsbsim/src/math/FGLocation.cpp','gym_jsbsim/jsbsim/src/math/FGMatrix33.cpp','gym_jsbsim/jsbsim/src/math/FGPropertyValue.cpp','gym_jsbsim/jsbsim/src/math/FGQuaternion.cpp','gym_jsbsim/jsbsim/src/math/FGRealValue.cpp','gym_jsbsim/jsbsim/src/math/FGTable.cpp','gym_jsbsim/jsbsim/src/math/FGCondition.cpp','gym_jsbsim/jsbsim/src/math/FGRungeKutta.cpp','gym_jsbsim/jsbsim/src/math/FGModelFunctions.cpp','gym_jsbsim/jsbsim/src/math/FGTemplateFunc.cpp','gym_jsbsim/jsbsim/src/input_output/FGGroundCallback.cpp','gym_jsbsim/jsbsim/src/input_output/FGPropertyManager.cpp','gym_jsbsim/jsbsim/src/input_output/FGScript.cpp','gym_jsbsim/jsbsim/src/input_output/FGXMLElement.cpp','gym_jsbsim/jsbsim/src/input_output/FGXMLParse.cpp','gym_jsbsim/jsbsim/src/input_output/FGfdmSocket.cpp','gym_jsbsim/jsbsim/src/input_output/FGOutputType.cpp','gym_jsbsim/jsbsim/src/input_output/FGOutputFG.cpp','gym_jsbsim/jsbsim/src/input_output/FGOutputSocket.cpp','gym_jsbsim/jsbsim/src/input_output/FGOutputFile.cpp','gym_jsbsim/jsbsim/src/input_output/FGOutputTextFile.cpp','gym_jsbsim/jsbsim/src/input_output/FGPropertyReader.cpp','gym_jsbsim/jsbsim/src/input_output/FGModelLoader.cpp','gym_jsbsim/jsbsim/src/input_output/FGInputType.cpp','gym_jsbsim/jsbsim/src/input_output/FGInputSocket.cpp','gym_jsbsim/jsbsim/src/input_output/FGUDPInputSocket.cpp','gym_jsbsim/jsbsim/src/simgear/props/props.cxx','gym_jsbsim/jsbsim/src/simgear/props/propertyObject.cxx','gym_jsbsim/jsbsim/src/simgear/xml/easyxml.cxx','gym_jsbsim/jsbsim/src/simgear/xml/xmlparse.c','gym_jsbsim/jsbsim/src/simgear/xml/xmltok.c','gym_jsbsim/jsbsim/src/simgear/xml/xmlrole.c','gym_jsbsim/jsbsim/src/simgear/magvar/coremag.cxx','gym_jsbsim/jsbsim/src/simgear/misc/sg_path.cxx','gym_jsbsim/jsbsim/src/simgear/misc/strutils.cxx','gym_jsbsim/jsbsim/src/simgear/io/iostreams/sgstream.cxx',],
                           include_dirs=['gym_jsbsim/jsbsim/src'],
                           libraries=libraries,
                           extra_compile_args=extra_compile_args,
                           language='c++')],
    package_data={'gym_jsbsim': ['docs/*','jsbsim/aircraft/*/*.xml','jsbsim/systems/*.xml','jsbsim/engine/*.xml']},
    install_requires=['cython>=0.25','gym>=0.12.5','shapely','geographiclib'],
    setup_requires=['cython>=0.25','gym>=0.12.5','shapely','geographiclib'])
