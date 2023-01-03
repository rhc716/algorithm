function cntToGrade(cnt) {
    var ret = 7 - cnt
    if (ret == 7)
        ret -= 1
    return ret
}

function solution(lottos, win_nums) {
    var cnt_zero = lottos.filter(x => x==0).length;
    var cnt_match = lottos.filter(value => win_nums.includes(value)).length;
    return [cntToGrade(cnt_match+cnt_zero), cntToGrade(cnt_match)]
}