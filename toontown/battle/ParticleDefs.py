from direct.particles import Particles, ForceGroup
from pandac.PandaModules import *

ParticleTable = {}


def particle(func):
    ParticleTable[func.func_name] = func


@particle
def gearExplosion(self):
    self.reset()
    self.setPos(0.000, 0.000, 4.600)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(40)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.2000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/gear")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.1600)
    p0.renderer.setFinalXScale(0.160)
    p0.renderer.setInitialYScale(0.1600)
    p0.renderer.setFinalYScale(0.160)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(9.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 9.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(3.2282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def smokeTest4(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(30)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(2.0000)
    p0.factory.setLifespanSpread(0.5000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
    p0.renderer.setUserAlpha(0.57)
    # Sprite parameters
    p0.renderer.addTextureFromFile(
        '../../ttmodels/src/maps/tt_t_efx_ext_smoke.tif')
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(2.0000)
    p0.renderer.setFinalXScale(4.0000)
    p0.renderer.setInitialYScale(2.0000)
    p0.renderer.setFinalYScale(4.0000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    p0.renderer.getColorInterpolationManager().addLinear(
        0.0, 1.0, Vec4(
            0.28235295414924622, 0.28235295414924622, 0.28235295414924622, 1.0), Vec4(
            0.28235295414924622, 0.28235295414924622, 0.28235295414924622, 1.0), 1)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(0.4000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 6.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)


@particle
def gearExplosionSmall(self):
    self.reset()
    self.setPos(0.000, 0.000, 4.600)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(6)
    p0.setBirthRate(0.4000)
    p0.setLitterSize(2)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/gear")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.112)
    p0.renderer.setFinalXScale(0.112)
    p0.renderer.setInitialYScale(0.112)
    p0.renderer.setFinalYScale(0.112)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(9.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 9.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(3.2282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def gearExplosionBig(self):
    self.reset()
    self.setPos(0.000, 0.000, 4.600)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(40)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.2000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/gear")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.1600)
    p0.renderer.setFinalXScale(0.160)
    p0.renderer.setInitialYScale(0.1600)
    p0.renderer.setFinalYScale(0.160)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(15.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 18.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.6282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def poundkey(self):
    self.reset()
    self.setPos(-0.500, 1.000, 3.100)
    self.setHpr(-180.000, -0.000, 180.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(0.20)
    p0.setLitterSize(3)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.5000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(20.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/poundsign")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0000)
    p0.renderer.setFinalXScale(0.600)
    p0.renderer.setInitialYScale(0.0000)
    p0.renderer.setFinalYScale(0.600)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(10.0000)
    p0.emitter.setAmplitudeSpread(3.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.200)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, 0.0000), 100.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)
    force0 = LinearJitterForce(4.5449, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def shred(self):
    self.reset()
    self.setPos(0.000, 3.000, 2.300)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.0600)
    p0.setLitterSize(3)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.9000)
    p0.factory.setLifespanSpread(0.4000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.2000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0160)
    p0.renderer.setFinalXScale(0.0240)
    p0.renderer.setInitialYScale(0.3200)
    p0.renderer.setFinalYScale(0.0800)
    p0.renderer.setNonanimatedTheta(5.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(1.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 3.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -7.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.6000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, 5.0000), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearSinkForce(
        Point3(0.0000, 0.0000, -8.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 14.5479, 155.9407, 1)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearNoiseForce(1.7000, 0)
    force2.setActive(1)
    f0.addForce(force2)
    force3 = LinearJitterForce(12.5698, 0)
    force3.setActive(1)
    f0.addForce(force3)
    self.addForceGroup(f0)


@particle
def withdrawal(self):
    self.reset()
    self.setPos(0.000, 10.000, 2.500)
    self.setHpr(-180.000, 0.000, 0.000)
    self.setScale(4.000, 4.000, 4.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(150)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.4000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAIN)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.04)
    p0.renderer.setFinalXScale(0.3125)
    p0.renderer.setInitialYScale(0.03)
    p0.renderer.setFinalYScale(0.25)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Line parameters
    #p0.renderer.setHeadColor(Vec4(1.00, 0.00, 0.00, 1.00))
    #p0.renderer.setTailColor(Vec4(1.00, 0.00, 0.00, 1.00))
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(-0.4000)
    p0.emitter.setAmplitudeSpread(0.1000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 1.5000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(1.7000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 1.0000, 0.0000), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def mumboJumboSmother(self):
    self.reset()
    self.setPos(0.000, 0.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(4)
    p0.setBirthRate(0.1100)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0300)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/mumbojumbo-iron")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.40)
    p0.renderer.setFinalXScale(0.10)
    p0.renderer.setInitialYScale(0.20)
    p0.renderer.setFinalYScale(0.05)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(-5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(1.5000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(37.2697, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def buzzWord(self):
    self.reset()
    self.setPos(0.000, 2.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(7)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/buzzwords-crash")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.300)
    p0.renderer.setFinalXScale(0.070)
    p0.renderer.setInitialYScale(0.200)
    p0.renderer.setFinalYScale(0.050)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(8.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 7.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.0010)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(64.5449, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def penSpill(self):
    self.reset()
    self.setPos(0.000, 0.000, -0.600)
    self.setHpr(0.000, 0.000, -90.000)
    self.setScale(1.100, 1.100, 1.100)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(70)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(2)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/raindrop")
    p0.renderer.setColor(Vec4(0, 0, 0, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.05)
    p0.renderer.setFinalXScale(0.000)
    p0.renderer.setInitialYScale(0.05)
    p0.renderer.setFinalYScale(0.000)
    p0.renderer.setNonanimatedTheta(90.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.2282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -99.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def fingerwag(self):
    self.reset()
    self.setPos(0.167, 0.692, 3.731)
    self.setHpr(90.000, -36.310, -0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("PointEmitter")
    p0.setPoolSize(250)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(2)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(2.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.6000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(410.7267)
    p0.factory.setTerminalVelocitySpread(2.3816)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(0.86)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/blah")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.400)
    p0.renderer.setFinalXScale(0.0200)
    p0.renderer.setInitialYScale(0.200)
    p0.renderer.setFinalYScale(0.0200)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(2.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Point parameters
    p0.emitter.setLocation(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('jfo')
    # Force parameters
    force0 = LinearJitterForce(4.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearSourceForce(
        Point3(
            0.0000,
            0.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        0.5000,
        1.0000,
        0)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearSinkForce(
        Point3(
            0.0000,
            1.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        1.0000,
        1.0000,
        1)
    force2.setActive(1)
    f0.addForce(force2)
    self.addForceGroup(f0)


@particle
def doubleTalkRight(self):
    self.reset()
    self.setPos(0.000, 3.000, 3.000)
    self.setHpr(-55.000, 0.000, 0.000)
    self.setScale(3.000, 3.000, 3.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(2)
    p0.setBirthRate(0.7000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.7000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/doubletalk-good")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(1.5)
    p0.renderer.setFinalXScale(1.5)
    p0.renderer.setInitialYScale(1.5)
    p0.renderer.setFinalYScale(1.5)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(12.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.6000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -8.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.0500)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(-6.000, -3.0000, 0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 1.5000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def filibusterSpray(self):
    self.reset()
    self.setPos(0.000, 3.000, 4.000)
    self.setHpr(0.000, 55.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1)
    p0.setBirthRate(0.400)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.2700)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/filibuster-cut")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.3 * 1.5)
    p0.renderer.setFinalXScale(0.75 * 1.5)
    p0.renderer.setInitialYScale(0.15 * 1.5)
    p0.renderer.setFinalYScale(0.25 * 1.5)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 8.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -1.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.1000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, -9.0000, -11.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 1.3661, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def fingerwag2(self):
    self.reset()
    self.setPos(0.228, 0.880, 4.314)
    self.setHpr(-2.862, -36.310, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(250)
    p0.setBirthRate(0.3000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(2.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.6000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(410.7267)
    p0.factory.setTerminalVelocitySpread(2.3816)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(0.86)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/blah")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.400)
    p0.renderer.setFinalXScale(0.0200)
    p0.renderer.setInitialYScale(0.200)
    p0.renderer.setFinalYScale(0.0200)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('jfo')
    # Force parameters
    self.addForceGroup(f0)


@particle
def schmoozeLowerSpray(self):
    self.reset()
    self.setPos(0.000, 6.600, 3.290)
    self.setHpr(0.000, -55.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1)
    p0.setBirthRate(0.400)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.900)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/schmooze-master")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.7)
    p0.renderer.setFinalXScale(0.07)
    p0.renderer.setInitialYScale(0.35)
    p0.renderer.setFinalYScale(0.07)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 11.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -1.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.1000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, -23.0000, 9.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 1.3661, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def brainStorm(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(70)
    p0.setBirthRate(0.4)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/brainstorm-box")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.600)
    p0.renderer.setFinalXScale(0.0400)
    p0.renderer.setInitialYScale(0.30)
    p0.renderer.setFinalYScale(0.0400)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 5.0000))
    # Disc parameters
    p0.emitter.setRadius(0.5000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(15.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def numberSpray(self):
    self.reset()
    self.setPos(0.000, 2.700, 3.900)
    self.setHpr(-180.000, 80.000, -180.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(2.1000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/fire")
    p0.renderer.setColor(Vec4(0.00, 0.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.125)
    p0.renderer.setFinalXScale(0.5)
    p0.renderer.setInitialYScale(0.2)
    p0.renderer.setFinalYScale(1.0)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.1000)
    p0.emitter.setAmplitudeSpread(2.5000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 9.1000, -4.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.500)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -3.5000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 2.5308, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, -10.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def demotionUnFreeze(self):
    self.reset()
    self.setPos(0.000, 0.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.000, 2.000, 2.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    # p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(70)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.04)
    p0.renderer.setFinalXScale(0.000)
    p0.renderer.setInitialYScale(0.04)
    p0.renderer.setFinalYScale(0.000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(4.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(0.6000)
    self.addParticles(p0)


@particle
def fillWithLeadSmother(self):
    self.reset()
    self.setPos(0.000, 0.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.0400)
    p0.setLitterSize(20)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0300)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/mumbojumbo-iron")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0100)
    p0.renderer.setFinalXScale(0.0100)
    p0.renderer.setInitialYScale(0.0100)
    p0.renderer.setFinalYScale(0.0100)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(-5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(1.1000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(37.2697, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def downsizeSpray(self):
    self.reset()
    self.setPos(0.000, 2.900, 3.400)
    self.setHpr(0.000, 60.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(50)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(7)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.3000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 1.00, 0.00, 0.80))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0750)
    p0.renderer.setFinalXScale(0.0375)
    p0.renderer.setInitialYScale(0.055)
    p0.renderer.setFinalYScale(0.024)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(4.9000)
    p0.emitter.setAmplitudeSpread(0.3000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 7.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.0010)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -5.3000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 2.5308, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, -7.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    force3 = LinearJitterForce(8.5449, 0)
    force3.setActive(1)
    f0.addForce(force3)
    self.addForceGroup(f0)


@particle
def fillWithLeadSpray(self):
    self.reset()
    self.setPos(0.000, 2.000, 2.300)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(150)
    p0.setBirthRate(0.0400)
    p0.setLitterSize(45)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(2.9000)
    p0.factory.setLifespanSpread(0.4000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.2000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.010)
    p0.renderer.setFinalXScale(0.010)
    p0.renderer.setInitialYScale(0.010)
    p0.renderer.setFinalYScale(0.010)
    p0.renderer.setNonanimatedTheta(5.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(1.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 5.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -7.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.01000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, 5.0000), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearSinkForce(
        Point3(0.0000, 0.0000, -8.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 14.5479, 155.9407, 1)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearNoiseForce(1.7000, 0)
    force2.setActive(1)
    f0.addForce(force2)
    force3 = LinearJitterForce(12.5698, 0)
    force3.setActive(1)
    f0.addForce(force3)
    self.addForceGroup(f0)


@particle
def reorgCloud(self):
    self.reset()
    self.setPos(0.000, 0.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.000, 2.000, 2.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(70)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 0.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.003)
    p0.renderer.setFinalXScale(0.000)
    p0.renderer.setInitialYScale(0.003)
    p0.renderer.setFinalYScale(0.000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(-1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)


@particle
def demotionFreeze(self):
    self.reset()
    self.setPos(0.000, 0.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.000, 2.000, 2.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(70)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.04)
    p0.renderer.setFinalXScale(0.000)
    p0.renderer.setInitialYScale(0.04)
    p0.renderer.setFinalYScale(0.000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(-1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)


@particle
def demotionSpray(self):
    self.reset()
    self.setPos(0.000, 4.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(150)
    p0.setBirthRate(0.0500)
    p0.setLitterSize(7)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.8000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.04)
    p0.renderer.setFinalXScale(0.009)
    p0.renderer.setInitialYScale(0.04)
    p0.renderer.setFinalYScale(0.009)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 6.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.8900)
    self.addParticles(p0)


@particle
def powertrip2(self):
    self.reset()
    self.setPos(-2.000, 2.500, 2.200)
    self.setHpr(-90.000, 0.000, 0.000)
    self.setScale(4.800, 4.800, 4.800)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.0800)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.2500)
    p0.factory.setLifespanSpread(0.050)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)

    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(0.1, 0.95, 0.2, 1.00))
    p0.renderer.setEdgeColor(Vec4(0, 0, 0, 1.00))
    p0.renderer.setBirthRadius(0.1000)
    p0.renderer.setDeathRadius(15.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.4000)
    p0.emitter.setAmplitudeSpread(1.1000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 1.1000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.120)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(-10.0000, 0.0000, 0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 2.5308, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, 0.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearJitterForce(4.5449, 0)
    force2.setActive(1)
    f0.addForce(force2)
    self.addForceGroup(f0)


@particle
def rollodexVortex(self):
    self.reset()
    self.setPos(-0.003, 2.465, 3.714)
    self.setHpr(84.924, 13.378, 56.334)  # (70.004, -75.422, 35.756)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("TangentRingEmitter")
    p0.setPoolSize(250)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(5)
    p0.setLitterSpread(3)
    p0.setSystemLifespan(5.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.2500)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(40.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/rollodex-card")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.4)
    p0.renderer.setFinalXScale(0.4)
    p0.renderer.setInitialYScale(0.3)
    p0.renderer.setFinalYScale(0.3)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Tangent Ring parameters
    p0.emitter.setRadius(0.7500)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forward')
    # Force parameters
    force0 = LinearSourceForce(
        Point3(
            0.0000,
            0.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        1.0000,
        1.0000,
        1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearSinkForce(
        Point3(
            0.0000,
            0.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        5.0000,
        6.0000,
        0)
    force1.setActive(0)
    f0.addForce(force1)
    force2 = LinearCylinderVortexForce(1.0000, 1.0000, 15.0000, 1.0000, 0)
    force2.setActive(1)
    f0.addForce(force2)
    force3 = LinearSourceForce(
        Point3(
            0.5000,
            0.0000,
            1.0000),
        LinearDistanceForce.FTONEOVERRCUBED,
        4.0000,
        4.0000,
        1)
    force3.setActive(1)
    f0.addForce(force3)
    self.addForceGroup(f0)


@particle
def pixieExplode(self):
    self.reset()
    self.setPos(2.500, 0.000, 2.500)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(3.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(7)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.5000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.0400)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0100)
    p0.emitter.setOffsetForce(Vec3(-0.1000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.5000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.1000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(2.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def guiltTrip(self):
    self.reset()
    self.setPos(-2.000, 2.500, 2.200)
    self.setHpr(-90.000, 0.000, 0.000)
    self.setScale(4.800, 4.800, 4.800)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.0800)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.4000)
    p0.factory.setLifespanSpread(0.000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)

    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.0, 0, 0, 0.9))
    p0.renderer.setEdgeColor(Vec4(0.8, 0.8, 0.8, 0.4))
    p0.renderer.setBirthRadius(0.1000)
    p0.renderer.setDeathRadius(15.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.4000)
    p0.emitter.setAmplitudeSpread(1.1000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 1.1000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.120)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(14.5449, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def soundBreak(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("ZSpinParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("PointEmitter")
    p0.setPoolSize(7)
    p0.setBirthRate(0.0500)
    p0.setLitterSize(3)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Z Spin factory parameters
    p0.factory.setInitialAngle(0.0000)
    p0.factory.setInitialAngleSpread(180.0000)
    p0.factory.enableAngularVelocity(1)
    p0.factory.setAngularVelocity(0.0000)
    p0.factory.setAngularVelocitySpread(0.0000)
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setTextureFromNode(
        "phase_5/models/props/uberSoundEffects", "**/break")
    # p0.renderer.addTextureFromFile('maps/break.tif')
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(1)
    p0.renderer.setInitialXScale(1.5000)
    p0.renderer.setFinalXScale(1.5000)
    p0.renderer.setInitialYScale(0.0000)
    p0.renderer.setFinalYScale(9.0000)
    p0.renderer.setNonanimatedTheta(319.3987)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Point parameters
    p0.emitter.setLocation(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)


@particle
def pixiePoof(self):
    self.reset()
    self.setPos(0.000, 0.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(200)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(2)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.04, 0.04, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.0272)
    p0.renderer.setDeathRadius(0.1872)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.200)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')


@particle
def waterfall(self):
    self.reset()
    self.setPos(0.000, 5.000, 2.300)
    self.setHpr(0.000, -45.000, 0.000)
    self.setScale(4.000, 4.000, 4.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(50)
    p0.setBirthRate(0.0500)
    p0.setLitterSize(4)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.1000)
    p0.factory.setLifespanSpread(0.1000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(0.1, 0.95, 0.2, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.00, 0.00, 0.00, 1.00))
    p0.renderer.setBirthRadius(0.0200)
    p0.renderer.setDeathRadius(0.0600)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.5000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.2000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -30.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 3.0400, 1.5000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def headShrinkCloud(self):
    self.reset()
    self.setPos(0.000, 0.000, 8.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.100)
    p0.setLitterSize(5)
    p0.setLitterSpread(3)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.3000)
    p0.factory.setLifespanSpread(0.100)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1, 0.84, 0, 1.00))
    p0.renderer.setEdgeColor(Vec4(1, 1, 1, 0.3))
    p0.renderer.setBirthRadius(0.1500)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(4.0000)
    p0.emitter.setAmplitudeSpread(2.5000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(0.0200)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(33.2697, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def firedFlame(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.500)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.500, 4.500, 2.500)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.0220)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.500)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/fire")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.15)
    p0.renderer.setFinalXScale(0.00025)
    p0.renderer.setInitialYScale(0.30)
    p0.renderer.setFinalYScale(0.00025)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 4.800))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -30.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.4000)
    self.addParticles(p0)


@particle
def spinSpray(self):
    self.reset()
    self.setPos(0.000, 6.500, 3.200)
    self.setHpr(50.000, -0.000, -90.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(70)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(9)
    p0.setLitterSpread(4)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.2000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 0.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.025)
    p0.renderer.setFinalXScale(0.05)
    p0.renderer.setInitialYScale(0.025)
    p0.renderer.setFinalYScale(0.05)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(6.0000)
    p0.emitter.setAmplitudeSpread(0.7000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.200)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -3.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 2.5308, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, 0.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def confetti(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(350)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(5)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.7000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    # p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/spark")
    # p0.renderer.addTextureFromFile('confetti.png')
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0070)
    p0.renderer.setFinalXScale(0.0500)
    p0.renderer.setInitialYScale(0.0070)
    p0.renderer.setFinalYScale(0.0500)
    p0.renderer.setNonanimatedTheta(145.0080)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # p0.renderer.getColorInterpolationManager().addSinusoid(0.0,0.60000002384185791,Vec4(1.0,0.0,0.0,1.0),Vec4(0.0,1.0,0.0,1.0),0.30000001192092896,1)
    # p0.renderer.getColorInterpolationManager().addSinusoid(0.5,1.0,Vec4(0.0,0.0,1.0,1.0),Vec4(1.0,0.0,0.0,1.0),0.30000001192092896,1)
    # p0.renderer.getColorInterpolationManager().addSinusoid(0.0,1.0,Vec4(1.0,0.0,0.0,1.0),Vec4(0.0,1.0,0.0,1.0),0.5,0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.0100)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('gravity')
    # Force parameters
    force0 = LinearJitterForce(5.0000, 0)
    force0.setVectorMasks(1, 1, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearSinkForce(
        Point3(0.0000, 0.0000, -0.8000),
        LinearDistanceForce.FTONEOVERRSQUARED, 0.5000, 1.0000, 1)
    force1.setVectorMasks(1, 1, 1)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def downsizeCloud(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(12)
    p0.setLitterSpread(4)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.3000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 1.00, 0.00, 0.80))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.015)
    p0.renderer.setFinalXScale(0.075)
    p0.renderer.setInitialYScale(0.0075)
    p0.renderer.setFinalYScale(0.055)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(-1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(2.70)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(14.5449, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def synergyWaterfall(self):
    self.reset()
    self.setPos(0.000, 5.000, 2.300)
    self.setHpr(0.000, -45.000, 0.000)
    self.setScale(4.000, 4.000, 4.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(50)
    p0.setBirthRate(0.0500)
    p0.setLitterSize(4)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.1000)
    p0.factory.setLifespanSpread(0.1000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/dollar-sign")
    p0.renderer.setColor(Vec4(0.00, 1.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.2)
    p0.renderer.setFinalXScale(0.2)
    p0.renderer.setInitialYScale(0.2)
    p0.renderer.setFinalYScale(0.2)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.5000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.2000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -15.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 3.0400, 1.5000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def calculate(self):
    self.reset()
    self.setPos(0.000, 2.5, 3.5)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(30)
    p0.setBirthRate(0.4000)
    p0.setLitterSize(3)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.9000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.3000)
    p0.factory.setTerminalVelocityBase(8.0000)
    p0.factory.setTerminalVelocitySpread(4.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/audit-plus")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0000)
    p0.renderer.setFinalXScale(0.400)
    p0.renderer.setInitialYScale(0.0000)
    p0.renderer.setFinalYScale(0.400)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(11.0000)
    p0.emitter.setAmplitudeSpread(2.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -2.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.5000)
    self.addParticles(p0)


@particle
def freezeAssets(self):
    self.reset()
    self.setPos(0.000, 0.000, -0.200)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(200)
    p0.setBirthRate(0.0800)
    p0.setLitterSize(7)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.7000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.064)
    p0.renderer.setFinalXScale(0.001)
    p0.renderer.setInitialYScale(0.064)
    p0.renderer.setFinalYScale(0.001)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(8.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 5.0000))
    # Disc parameters
    p0.emitter.setRadius(0.4500)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(15.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def spriteFiredFlecks(self):
    self.reset()
    self.setPos(0.000, 0.000, 2.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.200)
    p0.setLitterSize(2)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.100)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.025)
    p0.renderer.setFinalXScale(0.000)
    p0.renderer.setInitialYScale(0.025)
    p0.renderer.setFinalYScale(0.000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 4.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -4.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.5000)
    self.addParticles(p0)


@particle
def smile(self):
    self.reset()
    self.setPos(0.0, 0.0, 2.000)
    self.setHpr(85.000, 0.000, 90.000)
    #self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(400)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(200.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.1000)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)


@particle
def trickleLiquidate(self):
    self.reset()
    self.setPos(0.000, 0.000, -0.200)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(20)
    p0.setBirthRate(0.0800)
    p0.setLitterSize(3)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.4000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/raindrop")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.06)
    p0.renderer.setFinalXScale(0.06)
    p0.renderer.setInitialYScale(0.225)
    p0.renderer.setFinalYScale(0.225)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(16.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 6.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.4500)
    self.addParticles(p0)


@particle
def reorgSpray(self):
    self.reset()
    self.setPos(0.000, 5.700, 2.700)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(150)
    p0.setBirthRate(0.0500)
    p0.setLitterSize(7)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.8000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 0.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.003)
    p0.renderer.setFinalXScale(0.009)
    p0.renderer.setInitialYScale(0.003)
    p0.renderer.setFinalYScale(0.009)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 6.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.8900)
    self.addParticles(p0)


@particle
def liquidate(self):
    self.reset()
    self.setPos(0.000, 0.000, -0.200)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.0400)
    p0.setLitterSize(3)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.4000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/raindrop")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.06)
    p0.renderer.setFinalXScale(0.06)
    p0.renderer.setInitialYScale(0.225)
    p0.renderer.setFinalYScale(0.225)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(16.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 6.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.4500)
    self.addParticles(p0)


@particle
def mumboJumboSpray(self):
    self.reset()
    self.setPos(0.000, 4.000, 4.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 4.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(3)
    p0.setBirthRate(0.3000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.900)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/mumbojumbo-iron")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.40)
    p0.renderer.setFinalXScale(0.40)
    p0.renderer.setInitialYScale(0.20)
    p0.renderer.setFinalYScale(0.20)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(6.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -9.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.7000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(20.4636, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def gearExplosionWide(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(40)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.2000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/gear")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.1600)
    p0.renderer.setFinalXScale(0.1600)
    p0.renderer.setInitialYScale(0.1600)
    p0.renderer.setFinalYScale(0.1600)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(15.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 10.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -0.5000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.7500)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def pixieSpray(self):
    self.reset()
    self.setPos(2.00, 0.000, 4.00)
    self.setHpr(-90.000, 45.000, 0.000)
    self.setScale(4.000, 4.000, 4.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(50)
    p0.setBirthRate(0.0500)
    p0.setLitterSize(4)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.6000)
    p0.factory.setLifespanSpread(0.1000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.0200)
    p0.renderer.setDeathRadius(0.0500)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.5000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.100)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -30.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 3.0400, 1.5000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def synergy(self):
    self.reset()
    self.setPos(0, 7.8, 0.4)
    self.setHpr(90.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(250)
    p0.setBirthRate(0.0100)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.6)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/dollar-sign")
    p0.renderer.setColor(Vec4(0.00, 1.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.2)
    p0.renderer.setFinalXScale(0.2)
    p0.renderer.setInitialYScale(0.2)
    p0.renderer.setFinalYScale(0.2)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0697)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(-4.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(1.8607)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('jfo')
    # Force parameters
    force0 = LinearJitterForce(1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def soundWave(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(7.000, 7.000, 7.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("PointEmitter")
    p0.setPoolSize(128)
    p0.setBirthRate(0.4000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(10.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(0.0010)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(0.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setTextureFromNode(
        "phase_5/models/props/uberSoundEffects", "**/Circle")
    # p0.renderer.addTextureFromFile('maps/Circle.tif')
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0000)
    p0.renderer.setFinalXScale(3.0000)
    p0.renderer.setInitialYScale(0.0000)
    p0.renderer.setFinalYScale(3.0000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(1)
    p0.renderer.setColorBlendMode(
        ColorBlendAttrib.MAdd,
        ColorBlendAttrib.OIncomingAlpha,
        ColorBlendAttrib.OOne)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
    p0.emitter.setAmplitude(0.0100)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Point parameters
    p0.emitter.setLocation(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)


@particle
def tnt(self):
    self.reset()
    self.setPos(0.000, 0.000, -0.600)
    self.setHpr(0.000, 10.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(2)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.2000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/spark")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.3)
    p0.renderer.setFinalXScale(0.3)
    p0.renderer.setInitialYScale(0.3)
    p0.renderer.setFinalYScale(0.03)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Sparkle parameters
    #p0.renderer.setCenterColor(Vec4(0.78, 0.78, 0, 1.00))
    #p0.renderer.setEdgeColor(Vec4(0.78, 0.78, 0, 1.00))
    # p0.renderer.setBirthRadius(0.0600)
    # p0.renderer.setDeathRadius(0.0600)
    # p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.5000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.2282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -19.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def doubleTalkLeft(self):
    self.reset()
    self.setPos(0.000, 3.000, 3.000)
    self.setHpr(55.000, 0.000, 0.000)
    self.setScale(3.000, 3.000, 3.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(2)
    p0.setBirthRate(0.7000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.7000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/doubletalk-double")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(1.50)
    p0.renderer.setFinalXScale(1.50)
    p0.renderer.setInitialYScale(1.50)
    p0.renderer.setFinalYScale(1.50)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(12.000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.6000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -8.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.0500)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(6.000, -3.0000, 0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 1.5000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def pixieWall(self):
    self.reset()
    self.setPos(2.500, 0.000, 2.500)
    self.setHpr(-90.000, 90.000, -180.000)
    self.setScale(1.50)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(100)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.0000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.0400)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.5000)
    p0.emitter.setAmplitudeSpread(0.5000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 1.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -1.0000))
    # Disc parameters
    p0.emitter.setRadius(0.5000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearNoiseForce(0.0500, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def schmoozeUpperSpray(self):
    self.reset()
    self.setPos(0.000, 3.000, 4.000)
    self.setHpr(0.000, 55.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1)
    p0.setBirthRate(0.400)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.900)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/schmooze-master")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.7)
    p0.renderer.setFinalXScale(0.07)
    p0.renderer.setInitialYScale(0.35)
    p0.renderer.setFinalYScale(0.07)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 11.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -1.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.1000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, -23.0000, -9.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 1.3661, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def firedBaseFlame(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.500)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.500, 4.500, 2.500)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(150)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.100)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/fire")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.15)
    p0.renderer.setFinalXScale(0.50)
    p0.renderer.setInitialYScale(0.30)
    p0.renderer.setFinalYScale(0.50)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 2.200))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -30.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.4000)
    self.addParticles(p0)


@particle
def headShrinkSpray(self):
    self.reset()
    self.setPos(0.000, 2.900, 4.200)
    self.setHpr(0.000, 60.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60)  # 60)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(4)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.15)  # 1.1200)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1, 0.84, 0, 1.00))
    p0.renderer.setEdgeColor(Vec4(1, 1, 1, 0.3))
    p0.renderer.setBirthRadius(0.1500)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(12.0000)
    p0.emitter.setAmplitudeSpread(0.9000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 5.1000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.4800)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -4.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 2.5308, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, -7.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def jargonSpray(self):
    self.reset()
    self.setPos(0.000, 3.000, 4.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("LineEmitter")
    p0.setPoolSize(4)
    p0.setBirthRate(0.200)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.0000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/jargon-brow")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.40)
    p0.renderer.setFinalXScale(1.60)
    p0.renderer.setInitialYScale(0.10)
    p0.renderer.setFinalYScale(0.40)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 4.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -9.0000, 0.0000))
    # Line parameters
    p0.emitter.setEndpoint1(Point3(0.0000, 0.0000, 0.0000))
    p0.emitter.setEndpoint2(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(2.1279, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def legaleseSpray(self):
    self.reset()
    self.setPos(0.000, 2.000, 3.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(3.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/buzzwords-crash")
    p0.renderer.setColor(Vec4(0.00, 0.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(1.0)
    p0.renderer.setFinalXScale(1.8)
    p0.renderer.setInitialYScale(0.5)
    p0.renderer.setFinalYScale(0.9)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(8.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 7.0000, -1.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.0010)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(19.5449, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def powertrip(self):
    self.reset()
    self.setPos(-2.000, 2.500, 2.200)
    self.setHpr(-90.000, 0.000, 0.000)
    self.setScale(4.800, 4.800, 4.800)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.0800)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.2500)
    p0.factory.setLifespanSpread(0.050)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)

    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(0.1, 0.95, 0.2, 1.00))
    p0.renderer.setEdgeColor(Vec4(0, 0, 0, 1.00))
    p0.renderer.setBirthRadius(0.1000)
    p0.renderer.setDeathRadius(15.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.4000)
    p0.emitter.setAmplitudeSpread(1.1000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 1.1000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.120)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(
            10.0000,
            0.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        1.0000,
        2.5308,
        1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, 0.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearJitterForce(4.5449, 0)
    force2.setActive(1)
    f0.addForce(force2)
    self.addForceGroup(f0)


@particle
def spinEffect(self):
    self.reset()
    self.setScale(0.040, 0.040, 0.040)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(6)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.3000)
    p0.factory.setLifespanSpread(0.3000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/snow-particle")
    p0.renderer.setColor(Vec4(1.00, 0.00, 0.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.05)
    p0.renderer.setFinalXScale(0.05)
    p0.renderer.setInitialYScale(0.05)
    p0.renderer.setFinalYScale(0.05)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(4.000 * 1.2)
    p0.emitter.setAmplitudeSpread(1.000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -4.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.300)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 1.2000, 0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 20, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearJitterForce(5.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def restrainingOrderCloud(self):
    self.reset()
    self.setPos(0.000, 4.000, 3.000)
    self.setHpr(-180.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    # p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.0001)
    p0.setLitterSize(60)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.2000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/roll-o-dex")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.02)
    p0.renderer.setFinalXScale(0.001)
    p0.renderer.setInitialYScale(0.02)
    p0.renderer.setFinalYScale(0.001)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 6.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -18.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.8900)
    self.addParticles(p0)


@particle
def numberSpill(self):
    self.reset()
    self.setPos(0.900, 2.100, 1.90)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.100, 1.100, 1.100)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(6)
    p0.setBirthRate(0.3000)
    p0.setLitterSize(2)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(5.8000)
    p0.factory.setLifespanSpread(0.4000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/raindrop")
    p0.renderer.setColor(Vec4(0, 0, 0, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.2)
    p0.renderer.setFinalXScale(0.03)
    p0.renderer.setInitialYScale(0.3)
    p0.renderer.setFinalYScale(0.05)
    p0.renderer.setNonanimatedTheta(90.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.0000)
    p0.emitter.setAmplitudeSpread(1.300)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.3282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -33.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def headShrinkDrop(self):
    self.reset()
    self.setPos(0.000, 0.000, 7.500)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.000, 2.000, 2.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.1500)
    p0.setLitterSize(3)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.2000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1, 0.84, 0, 1.00))
    p0.renderer.setEdgeColor(Vec4(1, 1, 1, 0.3))
    p0.renderer.setBirthRadius(0.0400)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.300)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 4.0000))
    # Disc parameters
    p0.emitter.setRadius(0.2800)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(0.060, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def rollodexWaterfall(self):
    self.reset()
    self.setPos(-0.160, 2.942, 3.400)
    self.setHpr(89.908, -20.000, 179.476)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(20)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(3)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(5.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/rollodex-card")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.4)
    p0.renderer.setFinalXScale(0.4)
    p0.renderer.setInitialYScale(0.3)
    p0.renderer.setFinalYScale(0.3)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forward')
    # Force parameters
    force0 = LinearSourceForce(
        Point3(
            0.0000,
            0.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        1.0000,
        1.0000,
        1)
    force0.setActive(0)
    f0.addForce(force0)
    force1 = LinearSinkForce(
        Point3(
            0.0000,
            0.0000,
            10.0000),
        LinearDistanceForce.FTONEOVERRCUBED,
        2.9550,
        50.0000,
        1)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def rollodexStream(self):
    self.reset()
    self.setPos(0.107, 2.799, 3.400)
    self.setHpr(89.908, -20.000, 179.476)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("PointEmitter")
    p0.setPoolSize(60)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(2)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(5.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(3.0000)
    p0.factory.setMassSpread(2.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles",
        "**/rollodex-card")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.4)
    p0.renderer.setFinalXScale(0.4)
    p0.renderer.setInitialYScale(0.3)
    p0.renderer.setFinalYScale(0.3)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
    p0.emitter.setAmplitude(-15.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Point parameters
    p0.emitter.setLocation(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forward')
    # Force parameters
    force0 = LinearSourceForce(
        Point3(
            0.0000,
            0.0000,
            0.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        1.0000,
        1.0000,
        1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearJitterForce(19.1346, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def shiftSpray(self):
    self.reset()
    self.setPos(0.000, 5.000, 2.300)
    self.setHpr(0.000, -55.000, 0.000)
    self.setScale(9.000, 9.000, 9.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("LineEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(0.100)
    p0.setLitterSize(7)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.3000)
    p0.factory.setLifespanSpread(0.1000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 0.00, 0.9))
    p0.renderer.setEdgeColor(Vec4(1.00, 1.00, 0.00, 0.6))
    p0.renderer.setBirthRadius(0.0200)
    p0.renderer.setDeathRadius(0.0600)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.5000)
    p0.emitter.setAmplitudeSpread(0.5000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -3.0000, 0.0000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(
            0.0000,
            0.0000,
            96.0000),
        LinearDistanceForce.FTONEOVERRSQUARED,
        3.0400,
        1.5000,
        1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def pixieDrop(self):
    self.reset()
    self.setPos(0.000, 0.000, 6.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.000, 2.000, 2.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(150)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(7)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(2.2000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.0400)
    p0.renderer.setDeathRadius(0.0000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 4.0000))
    # Disc parameters
    p0.emitter.setRadius(0.3000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearJitterForce(3.6003, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def hotAirSpray(self):
    self.reset()
    self.setPos(0.000, 2.500, 3.200)  # originally (0,4,4)
    self.setHpr(-180.000, 80.000, -180.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(10)
    p0.setBirthRate(0.2000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.6000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/fire")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.6)
    p0.renderer.setFinalXScale(0.3)
    p0.renderer.setInitialYScale(0.6)
    p0.renderer.setFinalYScale(0.3)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 5.1000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, -4.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.0200)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -4.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 1.0000, 2.5308, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, -10.0000, 0.0000), 1.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def resistanceEffectSparkle(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(500)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(500)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(3.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setEdgeColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setBirthRadius(0.2000)
    p0.renderer.setDeathRadius(0.1000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(20.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(2.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def tt_p_efx_rocketLaunchFire(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("LineEmitter")
    p0.setPoolSize(50)
    p0.setBirthRate(0.0100)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.1000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(0.69)
    # Sprite parameters
    # p0.renderer.addTextureFromFile('../../ttmodels/src/maps/tt_t_efx_fireball.tif')
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(2.0000)
    p0.renderer.setFinalXScale(4.0000)
    p0.renderer.setInitialYScale(1.0000)
    p0.renderer.setFinalYScale(4.0000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    p0.renderer.getColorInterpolationManager().addLinear(
        0.10999999940395355, 1.0, Vec4(
            1.0, 1.0, 1.0, 1.0), Vec4(
            0.729411780834198, 0.40392157435417175, 0.11372549086809158, 1.0), 1)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, -10.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Line parameters
    p0.emitter.setEndpoint1(Point3(1.0000, 0.0000, 0.0000))
    p0.emitter.setEndpoint2(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Gravity')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, 2.5000), 1.0000, 0)
    force0.setVectorMasks(1, 1, 1)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, 0.0000, -3.0000), 5.0000, 0)
    force1.setVectorMasks(1, 1, 1)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def icetnt(self):
    self.reset()
    self.setPos(0.000, 0.000, -0.000)
    self.setHpr(0.000, 10.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(2)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.2000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/spark")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.3)
    p0.renderer.setFinalXScale(0.3)
    p0.renderer.setInitialYScale(0.3)
    p0.renderer.setFinalYScale(0.03)
    p0.renderer.setNonanimatedTheta(20.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Sparkle parameters
    #p0.renderer.setCenterColor(Vec4(0.78, 0.78, 0, 1.00))
    #p0.renderer.setEdgeColor(Vec4(0.78, 0.78, 0, 1.00))
    # p0.renderer.setBirthRadius(0.0600)
    # p0.renderer.setDeathRadius(0.0600)
    # p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.5000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.2282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -19.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def resistanceEffectSprite(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(50)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(50)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(3.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.5000)
    p0.renderer.setFinalXScale(0.5000)
    p0.renderer.setInitialYScale(0.5000)
    p0.renderer.setFinalYScale(0.5000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(20.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(2.0000)
    self.addParticles(p0)
    p1 = Particles.Particles('particles-2')
    # Particles parameters
    p1.setFactory("PointParticleFactory")
    p1.setRenderer("SpriteParticleRenderer")
    p1.setEmitter("SphereVolumeEmitter")
    p1.setPoolSize(50)
    p1.setBirthRate(0.1000)
    p1.setLitterSize(50)
    p1.setLitterSpread(0)
    p1.setSystemLifespan(0.0000)
    p1.setLocalVelocityFlag(1)
    p1.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p1.factory.setLifespanBase(3.0000)
    p1.factory.setLifespanSpread(0.0000)
    p1.factory.setMassBase(1.0000)
    p1.factory.setMassSpread(0.0000)
    p1.factory.setTerminalVelocityBase(400.0000)
    p1.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p1.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p1.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p1.renderer.setXScaleFlag(0)
    p1.renderer.setYScaleFlag(0)
    p1.renderer.setAnimAngleFlag(0)
    p1.renderer.setInitialXScale(0.5000)
    p1.renderer.setFinalXScale(0.5000)
    p1.renderer.setInitialYScale(0.5000)
    p1.renderer.setFinalYScale(0.5000)
    p1.renderer.setNonanimatedTheta(0.0000)
    p1.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p1.renderer.setAlphaDisable(0)
    # Emitter parameters
    p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p1.emitter.setAmplitude(20.0000)
    p1.emitter.setAmplitudeSpread(0.0000)
    p1.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p1.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p1.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p1.emitter.setRadius(2.0000)
    self.addParticles(p1)
    p2 = Particles.Particles('particles-3')
    # Particles parameters
    p2.setFactory("PointParticleFactory")
    p2.setRenderer("SpriteParticleRenderer")
    p2.setEmitter("SphereVolumeEmitter")
    p2.setPoolSize(50)
    p2.setBirthRate(0.1000)
    p2.setLitterSize(50)
    p2.setLitterSpread(0)
    p2.setSystemLifespan(0.0000)
    p2.setLocalVelocityFlag(1)
    p2.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p2.factory.setLifespanBase(3.0000)
    p2.factory.setLifespanSpread(0.0000)
    p2.factory.setMassBase(1.0000)
    p2.factory.setMassSpread(0.0000)
    p2.factory.setTerminalVelocityBase(400.0000)
    p2.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p2.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p2.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p2.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p2.renderer.setXScaleFlag(0)
    p2.renderer.setYScaleFlag(0)
    p2.renderer.setAnimAngleFlag(0)
    p2.renderer.setInitialXScale(0.5000)
    p2.renderer.setFinalXScale(0.5000)
    p2.renderer.setInitialYScale(0.5000)
    p2.renderer.setFinalYScale(0.5000)
    p2.renderer.setNonanimatedTheta(0.0000)
    p2.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p2.renderer.setAlphaDisable(0)
    # Emitter parameters
    p2.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p2.emitter.setAmplitude(20.0000)
    p2.emitter.setAmplitudeSpread(0.0000)
    p2.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p2.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p2.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p2.emitter.setRadius(2.0000)
    self.addParticles(p2)
    p3 = Particles.Particles('particles-4')
    # Particles parameters
    p3.setFactory("PointParticleFactory")
    p3.setRenderer("SpriteParticleRenderer")
    p3.setEmitter("SphereVolumeEmitter")
    p3.setPoolSize(50)
    p3.setBirthRate(0.1000)
    p3.setLitterSize(50)
    p3.setLitterSpread(0)
    p3.setSystemLifespan(0.0000)
    p3.setLocalVelocityFlag(1)
    p3.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p3.factory.setLifespanBase(3.0000)
    p3.factory.setLifespanSpread(0.0000)
    p3.factory.setMassBase(1.0000)
    p3.factory.setMassSpread(0.0000)
    p3.factory.setTerminalVelocityBase(400.0000)
    p3.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p3.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p3.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p3.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p3.renderer.setXScaleFlag(0)
    p3.renderer.setYScaleFlag(0)
    p3.renderer.setAnimAngleFlag(0)
    p3.renderer.setInitialXScale(0.5000)
    p3.renderer.setFinalXScale(0.5000)
    p3.renderer.setInitialYScale(0.5000)
    p3.renderer.setFinalYScale(0.5000)
    p3.renderer.setNonanimatedTheta(0.0000)
    p3.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p3.renderer.setAlphaDisable(0)
    # Emitter parameters
    p3.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p3.emitter.setAmplitude(20.0000)
    p3.emitter.setAmplitudeSpread(0.0000)
    p3.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p3.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p3.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p3.emitter.setRadius(2.0000)
    self.addParticles(p3)
    p4 = Particles.Particles('particles-5')
    # Particles parameters
    p4.setFactory("PointParticleFactory")
    p4.setRenderer("SpriteParticleRenderer")
    p4.setEmitter("SphereVolumeEmitter")
    p4.setPoolSize(50)
    p4.setBirthRate(0.1000)
    p4.setLitterSize(50)
    p4.setLitterSpread(0)
    p4.setSystemLifespan(0.0000)
    p4.setLocalVelocityFlag(1)
    p4.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p4.factory.setLifespanBase(3.0000)
    p4.factory.setLifespanSpread(0.0000)
    p4.factory.setMassBase(1.0000)
    p4.factory.setMassSpread(0.0000)
    p4.factory.setTerminalVelocityBase(400.0000)
    p4.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p4.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p4.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p4.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p4.renderer.setXScaleFlag(0)
    p4.renderer.setYScaleFlag(0)
    p4.renderer.setAnimAngleFlag(0)
    p4.renderer.setInitialXScale(0.5000)
    p4.renderer.setFinalXScale(0.5000)
    p4.renderer.setInitialYScale(0.5000)
    p4.renderer.setFinalYScale(0.5000)
    p4.renderer.setNonanimatedTheta(0.0000)
    p4.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p4.renderer.setAlphaDisable(0)
    # Emitter parameters
    p4.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p4.emitter.setAmplitude(20.0000)
    p4.emitter.setAmplitudeSpread(0.0000)
    p4.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p4.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p4.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p4.emitter.setRadius(2.0000)
    self.addParticles(p4)
    p5 = Particles.Particles('particles-6')
    # Particles parameters
    p5.setFactory("PointParticleFactory")
    p5.setRenderer("SpriteParticleRenderer")
    p5.setEmitter("SphereVolumeEmitter")
    p5.setPoolSize(50)
    p5.setBirthRate(0.1000)
    p5.setLitterSize(50)
    p5.setLitterSpread(0)
    p5.setSystemLifespan(0.0000)
    p5.setLocalVelocityFlag(1)
    p5.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p5.factory.setLifespanBase(3.0000)
    p5.factory.setLifespanSpread(0.0000)
    p5.factory.setMassBase(1.0000)
    p5.factory.setMassSpread(0.0000)
    p5.factory.setTerminalVelocityBase(400.0000)
    p5.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p5.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p5.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p5.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p5.renderer.setXScaleFlag(0)
    p5.renderer.setYScaleFlag(0)
    p5.renderer.setAnimAngleFlag(0)
    p5.renderer.setInitialXScale(0.5000)
    p5.renderer.setFinalXScale(0.5000)
    p5.renderer.setInitialYScale(0.5000)
    p5.renderer.setFinalYScale(0.5000)
    p5.renderer.setNonanimatedTheta(0.0000)
    p5.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p5.renderer.setAlphaDisable(0)
    # Emitter parameters
    p5.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p5.emitter.setAmplitude(20.0000)
    p5.emitter.setAmplitudeSpread(0.0000)
    p5.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p5.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p5.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p5.emitter.setRadius(2.0000)
    self.addParticles(p5)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def splashlines(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(40)
    p0.setBirthRate(1000)
    p0.setLitterSize(40)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(2.0)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(Vec4(0.02, 0.67, 0.92, 1.00))
    p0.renderer.setTailColor(Vec4(1.00, 1.00, 1.00, 1.00))
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(9.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 9.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, -2.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(3.2282)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0100, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def resistanceEffectBean(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("GeomParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(20)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(20)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(3.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Geom parameters
    # p0.renderer.setGeomNode(jellybean4.egg)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(20.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(2.0000)
    self.addParticles(p0)
    p1 = Particles.Particles('particles-2')
    # Particles parameters
    p1.setFactory("PointParticleFactory")
    p1.setRenderer("GeomParticleRenderer")
    p1.setEmitter("SphereVolumeEmitter")
    p1.setPoolSize(20)
    p1.setBirthRate(0.1000)
    p1.setLitterSize(20)
    p1.setLitterSpread(0)
    p1.setSystemLifespan(0.0000)
    p1.setLocalVelocityFlag(1)
    p1.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p1.factory.setLifespanBase(3.0000)
    p1.factory.setLifespanSpread(0.0000)
    p1.factory.setMassBase(1.0000)
    p1.factory.setMassSpread(0.0000)
    p1.factory.setTerminalVelocityBase(400.0000)
    p1.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p1.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p1.renderer.setUserAlpha(1.00)
    # Geom parameters
    # p1.renderer.setGeomNode(jellybean4.egg)
    # Emitter parameters
    p1.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p1.emitter.setAmplitude(20.0000)
    p1.emitter.setAmplitudeSpread(0.0000)
    p1.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p1.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p1.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p1.emitter.setRadius(2.0000)
    self.addParticles(p1)
    p2 = Particles.Particles('particles-3')
    # Particles parameters
    p2.setFactory("PointParticleFactory")
    p2.setRenderer("GeomParticleRenderer")
    p2.setEmitter("SphereVolumeEmitter")
    p2.setPoolSize(20)
    p2.setBirthRate(0.1000)
    p2.setLitterSize(20)
    p2.setLitterSpread(0)
    p2.setSystemLifespan(0.0000)
    p2.setLocalVelocityFlag(1)
    p2.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p2.factory.setLifespanBase(3.0000)
    p2.factory.setLifespanSpread(0.0000)
    p2.factory.setMassBase(1.0000)
    p2.factory.setMassSpread(0.0000)
    p2.factory.setTerminalVelocityBase(400.0000)
    p2.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p2.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p2.renderer.setUserAlpha(1.00)
    # Geom parameters
    # p2.renderer.setGeomNode(jellybean4.egg)
    # Emitter parameters
    p2.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p2.emitter.setAmplitude(20.0000)
    p2.emitter.setAmplitudeSpread(0.0000)
    p2.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p2.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p2.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p2.emitter.setRadius(2.0000)
    self.addParticles(p2)
    p3 = Particles.Particles('particles-4')
    # Particles parameters
    p3.setFactory("PointParticleFactory")
    p3.setRenderer("GeomParticleRenderer")
    p3.setEmitter("SphereVolumeEmitter")
    p3.setPoolSize(20)
    p3.setBirthRate(0.1000)
    p3.setLitterSize(20)
    p3.setLitterSpread(0)
    p3.setSystemLifespan(0.0000)
    p3.setLocalVelocityFlag(1)
    p3.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p3.factory.setLifespanBase(3.0000)
    p3.factory.setLifespanSpread(0.0000)
    p3.factory.setMassBase(1.0000)
    p3.factory.setMassSpread(0.0000)
    p3.factory.setTerminalVelocityBase(400.0000)
    p3.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p3.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p3.renderer.setUserAlpha(1.00)
    # Geom parameters
    # p3.renderer.setGeomNode(jellybean4.egg)
    # Emitter parameters
    p3.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p3.emitter.setAmplitude(20.0000)
    p3.emitter.setAmplitudeSpread(0.0000)
    p3.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p3.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p3.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p3.emitter.setRadius(2.0000)
    self.addParticles(p3)
    p4 = Particles.Particles('particles-5')
    # Particles parameters
    p4.setFactory("PointParticleFactory")
    p4.setRenderer("GeomParticleRenderer")
    p4.setEmitter("SphereVolumeEmitter")
    p4.setPoolSize(20)
    p4.setBirthRate(0.1000)
    p4.setLitterSize(20)
    p4.setLitterSpread(0)
    p4.setSystemLifespan(0.0000)
    p4.setLocalVelocityFlag(1)
    p4.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p4.factory.setLifespanBase(3.0000)
    p4.factory.setLifespanSpread(0.0000)
    p4.factory.setMassBase(1.0000)
    p4.factory.setMassSpread(0.0000)
    p4.factory.setTerminalVelocityBase(400.0000)
    p4.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p4.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p4.renderer.setUserAlpha(1.00)
    # Geom parameters
    # p4.renderer.setGeomNode(jellybean4.egg)
    # Emitter parameters
    p4.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p4.emitter.setAmplitude(20.0000)
    p4.emitter.setAmplitudeSpread(0.0000)
    p4.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 20.0000))
    p4.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p4.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p4.emitter.setRadius(2.0000)
    self.addParticles(p4)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 95.0000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def tt_p_efx_rocketLaunchSmoke(self):
    self.reset()
    self.setPos(0.000, 0.000, 16.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(2.000, 2.000, 3.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(300)
    p0.setBirthRate(0.1000)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.0000)
    p0.factory.setLifespanSpread(0.1000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
    p0.renderer.setUserAlpha(0.47)
    # Sprite parameters
    # p0.renderer.addTextureFromFile('../../ttmodels/src/maps/tt_t_efx_smoke.tif')
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(2.0000)
    p0.renderer.setFinalXScale(4.0000)
    p0.renderer.setInitialYScale(1.0000)
    p0.renderer.setFinalYScale(4.0000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    p0.renderer.getColorInterpolationManager().addLinear(
        0.0, 1.0, Vec4(
            1.0, 1.0, 1.0, 1.0), Vec4(
            0.58823531866073608, 0.58823531866073608, 0.58823531866073608, 1.0), 1)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(0.4000)
    p0.emitter.setAmplitudeSpread(2.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, -5.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Gravity')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, 2.5000), 1.0000, 0)
    force0.setVectorMasks(1, 1, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


@particle
def sparks(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("LineEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(8)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.256)
    p0.renderer.setFinalXScale(0.0000)
    p0.renderer.setInitialYScale(0.256)
    p0.renderer.setFinalYScale(0.0000)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(1)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
    p0.emitter.setAmplitude(0.0000)
    p0.emitter.setAmplitudeSpread(10.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 1.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 1.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Line parameters
    p0.emitter.setEndpoint1(Point3(0.5000, 5.0000, -0.5000))
    p0.emitter.setEndpoint2(Point3(0.75000, -5.0000, 2.5000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('sparkforces')
    # Force parameters
    force0 = LinearVectorForce(Vec3(1.0000, 0.0000, 0.0000), -50.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, -1.0000, 0.0000), 100.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearVectorForce(Vec3(0.0000, 0.0000, -1.0000), 20.0000, 0)
    force2.setActive(1)
    f0.addForce(force2)
    force3 = LinearJitterForce(50.0000, 0)
    force3.setActive(1)
    f0.addForce(force3)
    self.addForceGroup(f0)


@particle
def drift(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("ZSpinParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("PointEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0750)
    p0.setLitterSize(7)
    p0.setLitterSpread(2)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.1750)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Z Spin factory parameters
    p0.factory.enableAngularVelocity(1)
    p0.factory.setInitialAngle(0.0000)
    p0.factory.setInitialAngleSpread(45.0000)
    p0.factory.setFinalAngle(0.0000)
    p0.factory.setFinalAngleSpread(0.0000)
    p0.factory.setAngularVelocity(0.0000)
    p0.factory.setAngularVelocitySpread(90.0000)
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(0.50)
    # Sprite parameters
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(1)
    p0.renderer.setInitialXScale(0.375)
    p0.renderer.setFinalXScale(0.750)
    p0.renderer.setInitialYScale(0.375)
    p0.renderer.setFinalYScale(0.750)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # p0.renderer.setColorBlendMode(ColorBlendAttrib.MAdd,ColorBlendAttrib.OIncomingAlpha,ColorBlendAttrib.OOneMinusIncomingAlpha)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETEXPLICIT)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setLocation(Point3(0.0000, 0.0000, 0.0000))
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Smoke')
    # Force parameters
    force0 = LinearVectorForce(Vec3(1.0000, 0.0000, 0.0000), 0.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearVectorForce(Vec3(0.0000, -1.0000, 0.0000), 100.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    force2 = LinearVectorForce(Vec3(0.0000, 0.0000, 1.0000), 50.0000, 0)
    force2.setActive(1)
    f0.addForce(force2)
    force4 = LinearJitterForce(100.0000, 0)
    force4.setActive(1)
    f0.addForce(force4)
    self.addForceGroup(f0)


@particle
def snowdisk(self):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("ZSpinParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(4.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Z Spin factory parameters
    p0.factory.setInitialAngle(0.0000)
    p0.factory.setInitialAngleSpread(10.0000)
    p0.factory.enableAngularVelocity(1)
    p0.factory.setAngularVelocity(0.0000)
    p0.factory.setAngularVelocitySpread(500.0000)
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAIN)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_8/models/props/snowflake_particle", "**/p1_2")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(0)
    p0.renderer.setYScaleFlag(0)
    p0.renderer.setAnimAngleFlag(1)
    p0.renderer.setInitialXScale(0.03125)
    p0.renderer.setFinalXScale(0.50)
    p0.renderer.setInitialYScale(0.03125)
    p0.renderer.setFinalYScale(0.50)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(0.1000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(50.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('gravity')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, -1.0000), 1.5000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    force1 = LinearJitterForce(10.0000, 0)
    force1.setActive(1)
    f0.addForce(force1)
    self.addForceGroup(f0)


@particle
def bossCogFrontAttack(self):
    self.reset()
    self.setPos(0.000, 0.000, 4.600)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("SphereSurfaceEmitter")
    p0.setPoolSize(200)
    p0.setBirthRate(0.0050)
    p0.setLitterSize(1)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(1.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAUSER)
    p0.renderer.setUserAlpha(1.00)
    # Sprite parameters
    p0.renderer.setIgnoreScale(1)
    p0.renderer.setTextureFromNode(
        "phase_3.5/models/props/suit-particles", "**/gear")
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.150)
    p0.renderer.setFinalXScale(0.300)
    p0.renderer.setInitialYScale(0.150)
    p0.renderer.setFinalYScale(0.300)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, -10.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Surface parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forces')
    # Force parameters
    force0 = LinearSinkForce(
        Point3(0.0000, 0.0000, -79.0000),
        LinearDistanceForce.FTONEOVERRSQUARED, 15.9701, 50.0000, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)
