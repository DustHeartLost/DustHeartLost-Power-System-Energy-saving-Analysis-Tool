class Data(object):
    def __init__(self,id,name,capacity,consume_1,consume_2,consume_3,consume_4):
        self.id=id
        self.name=name
        self.capacity=capacity
        #负荷
        self.load_1=1
        self.load_2=0.75
        self.load_3=0.5
        self.load_4=0.4
        #煤耗
        self.consume_1 = consume_1
        self.consume_2 = consume_2
        self.consume_3 = consume_3
        self.consume_4 = consume_4

        self.power_self_1=0
        self.power_self_2=0
        self.power_self_3=0
        self.power_self_4=0

        self.consume_coal_1 = 0
        self.consume_coal_2 = 0
        self.consume_coal_3 = 0
        self.consume_coal_4 = 0

    def calculate_power(self,state,input):
        #计算每种负荷的发电量（GWh）
        #计算每种负荷的煤耗（吨）
        if state == 1:
            self.power_self_1=self.load_1*self.capacity*input/1000
            self.consume_coal_1 = self.consume_1*self.power_self_1
        elif state == 2:
            self.power_self_2=self.load_2*self.capacity*input/1000
            self.consume_coal_2 = self.consume_2 * self.power_self_2
        elif state == 3:
            self.power_self_3=self.load_3*self.capacity*input/1000
            self.consume_coal_3 = self.consume_3 * self.power_self_3
        elif state == 4:
            self.power_self_4=self.load_4*self.capacity*input/1000
            self.consume_coal_4 = self.consume_4 * self.power_self_4

        #计算总发电量
        self.power_all=self.power_self_1+self.power_self_2+self.power_self_3+self.power_self_4
        #计算总煤耗
        self.coal_all=self.consume_coal_1+self.consume_coal_2+self.consume_coal_3+self.consume_coal_4
        #年平均供电煤耗
        self.average_coal=self.coal_all/self.power_all