"""Check batched Grams against analytic diagonal and off-diagonal moments."""
import json
from pathlib import Path
from time import perf_counter
import mpmath as mm
from interval_source_gram import source_gram


def main():
    c = mm.iv
    c.dps = 80
    T = c.mpf(4)/5
    def column(source): return [(c.mpf(0),T,source)]
    one = column(([c.mpf(1)],[],[],[]))
    left = column(([],[c.mpf(1)],[],[]))
    right = column(([],[],[c.mpf(1)],[]))
    smooth = column(([],[],[],[c.mpf(1)]))
    shifted_smooth = column(([c.mpf(1)],[],[],[c.mpf(1)]))
    crossed = T*(2-c.pi**2/6)
    first_smooth = T*(2*c.log(2)-1)
    second_smooth = T*(2*c.log(2)**2-4*c.log(2)+2)
    tests = [
        ('endpoint_logs',[one,left,right],[[T,-T,-T],[-T,2*T,crossed],[-T,crossed,2*T]]),
        ('smooth_log_shared_cache',[one,smooth,shifted_smooth],
            [[T,first_smooth,T+first_smooth],
             [first_smooth,second_smooth,first_smooth+second_smooth],
             [T+first_smooth,first_smooth+second_smooth,T+2*first_smooth+second_smooth]])]
    records = []
    for name,columns,expected in tests:
        start = perf_counter()
        result = source_gram(c,columns,T,degree=64)
        for i in range(len(columns)):
            for j in range(len(columns)):
                actual,target = result[i][j],expected[i][j]
                assert actual.a <= target.b and target.a <= actual.b
                assert actual.b-actual.a < c.mpf('1e-27')
                assert actual == result[j][i]
        records.append(dict(case=name,dimension=len(columns),seconds=perf_counter()-start,
                            max_width=str(max(x.b-x.a for row in result for x in row))))
    report = dict(status='PASS',scope='batch moment contraction implementation; not the 95-column sign matrix',
                  interval_dps=80,records=records)
    Path(__file__).with_name('interval_source_gram_check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
