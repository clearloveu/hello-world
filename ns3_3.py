# #encoding=utf8
# from ns import core
# sim=core.Simulator
# n,K,Lambda,Mu=-1,0,2.0,2.0
# T_in,T_out=[],[]
# time_in,time_out=0,0
# r_eq=core.ExponentialRandomVariable()
# r_deq=core.ExponentialRandomVariable()
# r_eq.SetAttribute("Mean",core.DoubleValue(Lambda))
# r_deq.SetAttribute("Mean",core.DoubleValue(Mu))
# event_number=0              #定义处理的事件件数
# event_number_out=0
# isjudge=True
# def enq(argv):
#     global event_number,n,k,T_in,T_out,time_in,time_out,isjudge
#     if isjudge:
#         event_number+=1
#     if event_number<=100 and isjudge:   #处理100件事件完则停止向调度器增加事件
#         if event_number==100:
#             isjudge=False
#         now=sim.Now().GetSeconds()
#         time_eq=r_eq.GetValue()
#         time_in=now+time_eq
#         T_in.append(time_in)
#         K=1                #服务忙
#         n+=1
#         print"第%d个事件进入队列的时间是："%event_number,time_in,"K=",K,"n=",n
#         sim.Schedule(core.Seconds(time_eq),enq,now)
#         time_deq=r_deq.GetValue()
#         time_out=time_in+time_deq
#         T_out.append(time_out)
#         sim.Schedule(core.Seconds(time_deq),deq,T_in[event_number_out])
# def deq(argv):
#     global K,n,event_number_out
#     event_number_out+=1
#     # K=0的第一种情况是最后一个事件离开队列，第二种情况是某一个事件离开队列的时>间<后一个事件进入队列的时间
#     len_out=len(T_in)
#     if len_out==event_number_out:
#        K=0
#     if n!=0:
#         n-=1
#     print"第%d个事件离开队列的时间是："%event_number_out,T_out[(event_number_out-1)],"K=",K,"n=",n
# sim.Schedule(core.Seconds(0),enq,sim.Now().GetSeconds())
# sim.Run()
# sim.Destroy()



#encoding=utf8
from ns import core
sim=core.Simulator
n,K,Lambda,Mu=0,0,2.0,2.0
T_in,T_out=[],[]
time_in,time_out=0,0
r_eq=core.ExponentialRandomVariable()
r_deq=core.ExponentialRandomVariable()
r_eq.SetAttribute("Mean",core.DoubleValue(Lambda))
r_deq.SetAttribute("Mean",core.DoubleValue(Mu))
event_number=0              #定义处理的事件件数
event_number_out=0
num=-1
isjudge=True
def enq(argv):
    global event_number,n,k,T_in,T_out,time_in,time_out,isjudge,num
    if isjudge:
        event_number+=1
    if event_number<=100 and isjudge:   #处理100件事件完则停止向调度器增加事件
        if event_number==100:
            isjudge=False
        now=sim.Now().GetSeconds()
        time_eq=r_eq.GetValue()
        time_in=now+time_eq
        T_in.append(time_in)
        K=1                #服务忙
        num+=1
        if num>0:
            n+=1
        print"第%d个事件进入队列的时间是："%event_number,time_in,"K=",K,"n=",n
        sim.Schedule(core.Seconds(time_eq),enq,now)
        time_deq=r_deq.GetValue()
        time_out=time_in+time_deq
        T_out.append(time_out)
        sim.Schedule(core.Seconds(time_deq),deq,T_in[event_number_out])
def deq(argv):
    global K,n,event_number_out,num
    event_number_out+=1
    num-=1
    len_out=len(T_in)
    if len_out==event_number_out:K=0
    if n!=0:
        n-=1
    print"第%d个事件离开队列的时间是："%event_number_out,T_out[(event_number_out-1)],"K=",K,"n=",n,len_out,event_number_out
sim.Schedule(core.Seconds(0),enq,sim.Now().GetSeconds())
sim.Run()
sim.Destroy()


