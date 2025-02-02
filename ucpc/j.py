#test = 10^4, n = 10^6 -> 10^10 O(long??)
def result(state):
    l = len(state)
    cnt = 0
    idx = 0
    while idx < l:
        if(state[idx] == 'T'):
            if(idx + 1 == l):
                return -1
            if  state[idx + 1] == 'T':
                cnt += 1
                idx += 2
            else:
                con = 0
                i = idx + 1
                while i < l:
                    if(state[i] == 'H'):
                        con +=1
                        i += 1
                    else:
                        break
                if(con % 2 == 0 and i != l):
                    cnt += (con + 1)
                    idx = i + 1
                else:
                    return -1
        else:    
            idx += 1
    return cnt

test= int(input())
for _ in range(test):
    n = int(input())
    state = list(input().rstrip())
    print(result(state))