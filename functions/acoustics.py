#Acoustics related functions
import math;

#Predict the maximum diameter of a slot/square throat to avoid high frequency beaming (P.G 576/577 horn book) 
def SlotMaxBeam(fh, beam_width):
    ktr = 244; #-9dB for rectangular throat
    dt = ktr/math.sin(math.radians(beam_width/2))/fh;
    return dt;

#Predict the maximum diameter of a round throat to avoid high frequency beaming (P.G 576/577 horn book)
def RoundMaxBeam(fh, beam_width):
    ktr = 287; #-9dB for round throat
    dt = ktr/math.sin(math.radians(beam_width/2))/fh;
    return dt;

#Flare constant for a given cutoff for an exponential horn
def FcExp(fc):
    m = 4*math.pi*fc/344;
    return m;