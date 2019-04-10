import pandas as pd
import numpy as np
import copy

#separate class SPAM True/false
def separate(dataset):
    separated = {}
    for line in dataset:
        if line[-1] not in separated:
            separated[line[-1]] = []
        separated[line[-1]].append(line)
    return separated

#cal each mlp
def getMLP(titles,dataset):
    res = []
    for i in range(len(titles)-1):
        title = titles[i]

        # determin if a bool   ---discrete
        if isinstance(dataset[0][i], bool):
            ct = 0
            # count the true numbers
            for row in dataset:
                #number of false
                if not row[i]:
                    ct += 1
            res.append([ct/len(dataset),1-ct/len(dataset)])
            # print(res)

        # ---continus
        else:
            cur = []
            for row in dataset:
                cur.append(row[i])

            cur = np.array(cur)
            mean = np.mean(cur)
            var = np.std(cur)**2

            res.append((mean,var))

    return res


#print the parameter probaility
def printKML(MLP,titles,classify):
    for i in range(len(titles)-1):
        if isinstance(MLP[i], list):
            print('P({}={}|{}) = {}'.format(titles[i],'False', titles[-1] + '=' + classify, MLP[i][0]))
            print('P({}={}|{}) = {}'.format(titles[i], 'True', titles[-1] + '=' + classify, MLP[i][1]))
        else:
            print('P({}) = mean:{}, var:{}'.format(titles[i], MLP[i][0], MLP[i][1] ))

#calculate the probaility of continuous data
def calProOfCon(x,mean,var):
    pro = (1/(2*np.pi*var)**0.5) * np.exp(-(x-mean)**2/(2*var))
    return pro


# classify each row and return two probaility of each class
def classifyEach(row,paras):

    probabilities = {}
    for c in [False, True]:
        pro = 1
        for i in range(len(row)-1):
            if isinstance(row[i], bool) and not row[i] :
                pro *= paras[c][i][0]
            elif isinstance(row[i], bool) and row[i] :
                pro *= paras[c][i][1]
            else:
                pro *= calProOfCon(row[i],paras[c][i][0],paras[c][i][1])
        probabilities[c] = pro
    return probabilities


#classify the datas and select the answer
def classify(data,paras):

    res = []
    for row in data:
        probabilities = classifyEach(row[:-1],paras)
        cur = sorted(probabilities.items(),key=lambda x:-x[-1])
        res.append(cur[0][0])
    # print(res)
    return res


#cal the error rate
def calErrorRate(org,guess):
    ct = 0
    for i in range(len(org)):
        if org[i] != guess[i]:
            ct += 1
    error = ct/len(org)

    return error


def main():

    #question 1
    train_datas = pd.read_csv("q3.csv")
    titles = train_datas.columns[:].tolist()
    train_datas = np.array(train_datas[titles])

    s = separate(train_datas)
    MLP_True = getMLP(titles,s[True])
    MLP_False = getMLP(titles,s[False])

    paras = {}
    paras[False] = MLP_False
    paras[True] = MLP_True

    print(" ")
    printKML(MLP_False,titles,'False')
    print(" ")
    printKML(MLP_True,titles,'True')


    #question 2
    test_datas = pd.read_csv("q3b.csv")
    test_datas = np.array(test_datas[titles])
    org = test_datas[:,-1]

    # classify result
    guess = classify(test_datas,paras)
    #print
    errorRate = calErrorRate(org,guess)

    print('classification error rate: {}%'.format(errorRate * 100))

    #question 3
    for i in range(1,len(titles)-1):
        new_titles = titles[:i]
        newparas = copy.deepcopy(paras)
        newparas[True] = newparas[True][:i]
        newparas[False] = newparas[False][:i]
        newtest = test_datas[:,:i+1]

        newguess = classify(newtest, newparas)
        errorRate = calErrorRate(org, newguess)
        print(" ")
        print('{} parameters'.format(i),new_titles)
        print('classification error rate with {} parameters: {}%'.format(i,errorRate * 100))


main()


