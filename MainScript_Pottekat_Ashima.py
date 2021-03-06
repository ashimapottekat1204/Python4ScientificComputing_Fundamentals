# Energy And Environmental Technologies For Building Systems : Assignment 04, Step-2

# Submitted By : Ashima Pottekat

# Assignment Based On Exercise-1 From Topic 1.3 (Determine the overall unit thermal resistance and the overall heat transfer coefficient)
import os
os.chdir("C:/Users/ashis/Desktop/assignments")

import WallCalculation_Pottekat_Ashima as FC

print "This is the calculation for stud layer"
stud_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"woodStud_38mm_90mm","gypsumWallboard_13mm"]
    
Rtot_stud = FC.wallCalc_parallel(stud_layer)
    
Ustud = 1/Rtot_stud["R total"]
fstud = 0.25
Ustud_tot = fstud*Ustud

print "The total heat transfer coefficient on stud is " + str(Ustud) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on stud with 0.25 fraction area is " + str(Ustud_tot) + " (W/m^2 deg C)"

print "This is the calculation for insulation layer"
ins_layer = ["woodBevelLappedSliding_13mm_200mm","woodFiberboard_13mm",
"glassFiberIns_90mm","gypsumWallboard_13mm"]

Rtot_ins = FC.wallCalc_parallel(ins_layer)

Uins = 1/Rtot_ins["R total"]
fins = 0.75
Uins_tot = fins*Uins

print "The total heat transfer coefficient on insulation is " + str(Uins) + " (W/m^2 deg C)"
print "The total heat transfer coefficient on insulation with 0.75 fraction area is " + str(Uins_tot) + " (W/m^2 deg C)"

Utot = Ustud_tot + Uins_tot

print "Thus, the overall heat transfer coefficient of the wall is " + str(Utot) + " (W/m^2 deg C)"

print "This is the calculation for door"
door_layer = ["wood50mm"]
    
Rtot_door = FC.wallCalc_series(door_layer)

Udoor = 1/Rtot_door["R total"]
print "The total heat transfer coefficient for door " + str(Udoor) + " (W/m^2 deg C)"

print "This is the calculation for ceiling"
The_ceiling = ["specialRoofUrethaneRigidFoam"]
    
Rtot_ceiling = FC.wallCalc_series(The_ceiling)

Uceiling = 1/Rtot_ceiling["R total"]
print "The total heat transfer coefficient for ceiling " + str(Uceiling) + " (W/m^2 deg C)"

Tin = 20
Tout = -4.8

DT=Tin-Tout

print "The differential temperature between inside and outside of the wall is " + str(DT) + " (Deg C)"


A_wall = 105.8
A_door = 2.2
A_ceiling = 200

print "The total area of the wall is " + str(A_wall) + " (m^2)"
print "*********************************************************"

# Q total

Q = Utot*A_wall*DT

# change from Watt to KWatt

Qtot = Q/1000


