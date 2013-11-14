# -*- coding: utf-8 -*-

import datetime
import sys

#public class A {
#
#        static final long MAXD = 100000000000000000L; // 10^17
#        public static void main(String[] args) throws IOException {
#                    int n;
#                        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
#                        String sn = input.readLine();
#                        n = Integer.parseInt(sn);
#                    long[] b = new long[n];
#                    long[] t = new long[n];
#
#                    for (int i = 0; i < n; ++i) {
#                            String line = input.readLine();
#                            String[] vals = line.split(" ");
#                            b[i] = Integer.parseInt(vals[0]);
#                            t[i] = Integer.parseInt(vals[1]);
#                    }
#
#                    long goal;
#                        String sgoal = input.readLine();
#                        goal = Long.parseLong(sgoal);
#
#                    long l = 0, r = MAXD;
#                    while(l + 1 != r) {
#                        long cnt = 0, m = (l+r)/2;
#                        for (int i = 0; i < n && cnt <= MAXD; ++i) {
#                            if(m >= b[i])
#                                cnt += (m - b[i]) / t[i] + 1;
#                        }
#
#                        if(cnt < goal)
#                            l = m;
#                        else
#                            r = m;
#                    }
#
#                    System.out.println(r);
#        }
#
#}

# Input format
# Первая строка входного файла содержит целое число N – количество программистов (1 < N ≤ 105).
# В каждой из следующих N строк записаны через пробел 2 натуральных числа – Bi и Ti (1 ≤ Bi, Ti ≤ 1000),
# где Bi – время в часах от начала работы над проектом, когда i-ый программист совершит первый коммит, Ti – период в часах, с которым i-ый программист делает коммиты в VCS.
# И, наконец, в последней строке записано целое число M – номер юбилейного коммита (1 ≤ M ≤ 1012).
#
# Output format
# В выходной файл следует вывести одно целое число – час от начала работы над проектом (считая с первого), в который будет отправлен юбилейный коммит.

def main(args):
    print args

    return 0

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    main(sys.argv[1:])

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)
