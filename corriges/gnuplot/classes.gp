# gnuplot classes_complexite.gp

set terminal pngcairo size 1200,900
set output "classes_complexite.png"
set multiplot layout 2,1 title "Classes de complexité" font "Times New Roman,20"
set key off
set samples 200
set style data points
#
set title "n = 0..100"
set label 1 "2^x" at 7,95
set label 2 "x^2" at 10,85
set label 3 "x.log(x)" at 21,90
set label 4 "x" at 85,90
set label 5 "log(x)" at 85,8
plot [0:100] [0:100] 2**x, x**2, x*log(x), x, log(x)
#
set title "n = 0..500"
set label 1 "2^x" at 10,480
set label 2 "x^2" at 24,420
set label 3 "x.log(x)" at 70,450
set label 4 "x" at 430,450
set label 5 "log(x)" at 450, 30
plot [0:500] [0:500] 2**x, x**2, x*log(x), x, log(x)

