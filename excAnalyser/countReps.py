def countRepetition(previous_pose, current_pose, previous_state, flag):
    if current_pose[0][10][0] == 0 and current_pose[0][10][1] == 0:
        return 'Cannot detect any joint in the frame', previous_pose, previous_state, flag
    else:
        string, current_state = '', previous_state.copy()
        sdy,sdx = 0,0
        # Discard first 5 (0-4 indices) values, we don't need the value of nose, eye etc
        for i in range(5, 17):
            # The fancy text overlay
            string = string + keyValues[i] + ': '
            string = string + str('%.2f' % (current_pose[0][i][0])) + ' ' + str('%.2f' % current_pose[0][i][1]) + '\n'
            # If the difference is greater or lesser than tolerance or -tolerance sum it up or add 0 to sdx and sdy
            dx = (current_pose[0][i][0] - previous_pose[0][i][0])
            dy = (current_pose[0][i][1] - previous_pose[0][i][1])
            if(dx < tolerance and dx > (-1 * tolerance)):
                dx = 0
            if(dy < tolerance and dy > (-1 * tolerance)):
                dy = 0
            sdx += dx
            sdy += dy
        # if an overall average increase in value is detected set the current_state's bit to 1, if it decrease set it to 0
        # if it is between tolerance*3 and -tolerance*3, do nothing (then current_state will contain same value as previous)
        if(sdx > (tolerance*3)):
            current_state[0] = 1
        elif(sdx < (tolerance*-3)):
            current_state[0] = 0
        if(sdy > (tolerance*3)):
            current_state[1] = 1
        elif(sdy < (tolerance*-3)):
            current_state[1] = 0
        if(current_state != previous_state):
            flag = (flag + 1)%2
        return string, current_pose, current_state.copy(), flag
