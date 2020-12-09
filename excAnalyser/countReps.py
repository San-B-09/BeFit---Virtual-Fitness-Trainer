def countReps(phase_list, total_phases):
    mx=max(phase_list)
    if len(phase_list)<total_phases:
        return phase_list
    if mx<total_phases//2:
        return phase_list
    f_occ=phase_list.index(mx)
    phase_list.reverse()
    l_occ=len(phase_list)-phase_list.index(mx)-1
    phase_list.reverse()
    if (0 in phase_list[:f_occ]) and (0 in phase_list[l_occ:]):
        return [0]
    else:
        return phase_list