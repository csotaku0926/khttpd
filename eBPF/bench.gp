reset
set xlabel 'thread no.'
set ylabel 'time (ns)'
set title 'khttpd concurrent performance'
set term png enhanced font 'Verdana,10'
set output 'out.png'
set xrange [0:100000]
set yrange [0:1000000]

plot [0:][0:] \
'out.txt' using 1:2 with points title 'Avg. time elapsed'
