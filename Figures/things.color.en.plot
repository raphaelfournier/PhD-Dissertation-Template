set encoding utf8
set terminal postscript eps size 3.5,2.62 enhanced color font 'Helvetica,16' linewidth 2
set xdata time
set timefmt "%d-%m-%Y"
set format x "%Y-%m"
set xtics nomirror rotate by -45
set rmargin 5
set style line 2 lc 3
#set bmargin 8
#set decimalsign ','

#####
set output "something-weeks-coul-en.eps"
set yrange [0:12000000]
set y2range [0:50000]
set ytics nomirror
set xtics nomirror rotate by -45
set xlabel "day"
set ylabel "# occurences"
p "Data/vol_frac_weeks.data" u 1:2 w l axis x1y1 t 'all', "Data/vol_frac_weeks.data" u 1:3 w l axis x1y2 t 'specific'

set autoscale y

####
set output "anotherthing-week-coul-en.eps"
set xlabel "week"
set ylabel "fraction (in %)"
set xtics 15768000
set yrange [:0.95]
jan12 = "01-01-2012"
jan11 = "01-01-2011"
jan10 = "01-01-2010"
set arrow 2010 from jan10, graph 0 to jan10, graph 1 nohead
set arrow 2011 from jan11, graph 0 to jan11, graph 1 nohead
set arrow 2012 from jan12, graph 0 to jan12, graph 1 nohead
p "Data/window_168.weeks.data" u 1:($7/$6*100) w l t "users"
unset arrow

#####
set output "thirdthing-week-coul-en.eps"
#set size square 0.9,0.9
set xlabel "week"
set ylabel "things (millions)"
#jan12 = "01-01-2012"
jul11 = "01-07-2011"
jul10 = "01-07-2010"
may12 = "01-05-2012"
#set arrow 2010 from jul10, graph 0 to jul10, graph 1 nohead
#set arrow 2011 from jul11, graph 0 to jul11, graph 1 nohead
#set arrow 2012 from jan12, graph 0 to jan12, graph 1 nohead
#set label "2009" at "01-08-2009",3
#set label "2010" at "01-05-2010",3
#set label "2011" at "01-05-2011",3
#set label "2012" at "15-01-2012",3
#set format x ""
set ytics 2
p [:may12][:13] "Data/vol_frac_weeks.data" u 1:($2/1000000) w l t 'all'
