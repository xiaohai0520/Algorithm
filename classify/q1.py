import numpy as np
import pandas as pd  
import matplotlib.pyplot as plt

class hw1_1():

    def __init__(self,filepath):

        self.df = pd.read_csv(filepath)
        # self.df = pd.read_csv('Frogs.csv')
        self.alt = np.array(self.df[['MFCCs_10', 'MFCCs_17', 'Species']])
        self.HM10 = []
        self.HM17 = []
        self.HC10 = []
        self.HC17 = []
        for data in self.alt:
            if data[2] == 'HylaMinuta':
                self.HM10.append(data[0])
                self.HM17.append(data[1])
            else:
                self.HC10.append(data[0])
                self.HC17.append(data[1])

        self.HM10, self.HM17, self.HC10, self.HC17 = np.array(self.HM10), np.array(self.HM17), np.array(self.HC10), np.array(self.HC17)
        # print(self.HM17)

    def frog_scatter_plot(self):


        plt.figure()
        plt.scatter(self.HM10,self.HM17,s=10,c='red',label='HylaMinuta')
        plt.scatter(self.HC10,self.HC17, s=10, c='green', label='HypsiboasCinerascens')
        # plt.text(0,0,'red = HylaMinuta, green = HypsiboasCinerasce')
        plt.xlabel('MFCCs_10')
        plt.ylabel('MFCCs_17')
        plt.title('two kinds frogs')
        plt.show()



    def frog_histogram(self):

        # no 1
        plt.figure()
        plt.hist(self.HM10)
        plt.title('HylaMinuta')
        plt.xlabel('MFCCs_10')
        plt.ylabel('Count')
        plt.show()

        plt.figure()
        plt.hist(self.HM17)
        plt.title('HylaMinuta')
        plt.xlabel('MFCCs_17')
        plt.ylabel('Count')
        plt.show()

        plt.hist(self.HC10)
        plt.title('HypsiboasCinerascens')
        plt.xlabel('MFCCs_10')
        plt.ylabel('Count')
        plt.show()

        plt.hist(self.HC17)
        plt.title('HypsiboasCinerascens')
        plt.xlabel('MFCCs_17')
        plt.ylabel('Count')
        plt.show()



    def frog_line(self):
        HM10 = self.HM10
        HM17 = self.HM17
        HC10 = self.HC10
        HC17 = self.HC17

        HM10.sort()
        HM17.sort()
        HC10.sort()
        HC17.sort()

        xline = np.arange(0,len(HM10))

        plt.plot(xline,HM10)
        plt.xlabel('number')
        plt.ylabel('MFCCs_10')
        plt.title('HylaMinuta--MFCCs_10')
        plt.show()

        plt.plot(xline,HM17)
        plt.xlabel('number')
        plt.ylabel('MFCCs_17')
        plt.title('HylaMinuta--MFCCs_17')
        plt.show()

        xline = np.arange(0, len(HC10))
        plt.plot(xline,HC10)
        plt.xlabel('number')
        plt.ylabel('MFCCs_10')
        plt.title('HypsiboasCinerascens--MFCCs_10')
        plt.show()

        plt.plot(xline,HC17)
        plt.xlabel('number')
        plt.ylabel('MFCCs_17')
        plt.title('HypsiboasCinerascens--MFCCs_17')
        plt.show()


    def frog_box(self):

        plt.boxplot(self.HM10,sym ="o", whis = 1)
        plt.title('HylaMinuta--MFCCs_10')
        plt.show()

        plt.boxplot(self.HM17,sym ="o", whis = 1)
        plt.title('HylaMinuta--MFCCs_17')
        plt.show()

        plt.boxplot(self.HC10,sym ="o", whis = 1)
        plt.title('HypsiboasCinerascens--MFCCs_10')
        plt.show()

        plt.boxplot(self.HC17,sym ="o", whis = 1)
        plt.title('HypsiboasCinerascens--MFCCs_17')
        plt.show()

    # BAR
    def frog_bar(self):
        plt.figure()
        hm10_mean = np.mean(self.HM10)
        hm10_std = np.std(self.HM10)
        plt.bar(1,hm10_mean,yerr=hm10_std)
        plt.show()

        plt.figure()
        hm17_mean = np.mean(self.HM17)
        hm17_std = np.std(self.HM17)
        plt.bar(1,hm17_mean,yerr=hm17_std)
        plt.show()

        plt.figure()
        hc10_mean = np.mean(self.HC10)
        hc10_std = np.std(self.HC10)
        plt.bar(1,hc10_mean,yerr=hc10_std)
        plt.show()

        plt.figure()
        hc17_mean = np.mean(self.HC17)
        hc17_std = np.std(self.HC17)
        plt.bar(1,hc17_mean,yerr=hc17_std)
        plt.show()






    def cal(self):
        HM = []
        HC = []
        for data in self.alt:
            if data[2] == 'HylaMinuta':
                cur = data[:2]
                HM.append(cur)
            else:
                cur = data[:2]
                HC.append(cur)


        HM = np.array(HM)
        HC = np.array(HC)
        HM_mean10 = np.mean(self.HM10)
        HM_mean17 = np.mean(self.HM17)
        HM_cov = np.cov(HM.astype(float), rowvar=False)
        HM_std10 = np.std(self.HM10)
        HM_std17 = np.std(self.HM17)
        print(HM_mean10)
        print(HM_mean17)
        print(HM_cov)
        print(HM_std10)
        print(HM_std17)


        HC_mean10 = np.mean(self.HC10)
        HC_mean17 = np.mean(self.HC17)
        HC_cov = np.cov(HC.astype(float), rowvar=False)
        HC_std10 = np.std(self.HC10)
        HC_std17 = np.std(self.HC17)
        print(HC_mean10)
        print(HC_mean17)
        print(HC_cov)
        print(HC_std10)
        print(HC_std17)



def main():
    files = ['Frogs.csv','Frogs-subsample.csv']
    for file in files:
        h = hw1_1(file)
        h.frog_scatter_plot()
        h.frog_histogram()
        h.frog_line()
        h.frog_box()
        h.frog_bar()
        h.cal()
if __name__ == '__main__':
    main()
