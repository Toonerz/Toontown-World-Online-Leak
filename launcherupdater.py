import os
import urllib

print 'Removing old files'

if (os.path.exists('launcher.py')):
	os.unlink('launcher.py')
	

if (os.path.exists('gameupdater.py')):
	os.unlink('gameupdater.py')

if (os.path.exists('phaseupdater.py')):
	os.unlink('phaseupdater.py')
	
if (os.path.exists('phase_2.mf')):
	os.unlink('phase_2.mf')

print 'updating phase updater'
f = open('phaseupdater.py','wb'); f.write(urllib.urlopen('https://toontownworldonline.com/download/syst/phaseupdater.py').read()); f.close()
print 'patched phase updater!'

print 'updating game updater'
f = open('gameupdater.py','wb'); f.write(urllib.urlopen('https://toontownworldonline.com/download/syst/gameupdater.py').read()); f.close()
print 'patched game updater!'

print 'updating launcher'
f = open('launcher.py','wb'); f.write(urllib.urlopen('https://toontownworldonline.com/download/syst/launcher.py').read()); f.close()
print 'patched launcher!'

print 'updating phase_2'
f = open('phase_2.mf','wb'); f.write(urllib.urlopen('https://toontownworldonline.com/download/phase_2.mf').read()); f.close()
print 'patched phase_2!'