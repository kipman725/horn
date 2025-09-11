#Acoustics related functions
import math;

#Predict the maximum diameter of a slot/throat to avoid high frequency beaming (P.G 576/577 horn book)
def SlotMaxBeam(fh, beam_width):
    ktr = 244; #-9dB for rectangular throat
    dt = ktr/math.sin(math.radians(beam_width/2))/fh;
    return dt;