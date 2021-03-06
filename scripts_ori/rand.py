# Autogenerated with SMOP 
from smop.core import *
import ipdb
# 
    ipdb.set_trace()
    
#@function
def random_traj(traj=None,K=None,dis_threshold=None,*args,**kwargs):
    
varargin = random_traj.varargin
nargin = random_traj.nargin

#Implemented by Ruikun Luo
#Basic idea is from STOMP paper, only generate multiple random traj
#traj = N * D, where N is the traj length, D is the traj dimension
    
    ## Precompute part
#### A, R_1, M
#### N: traj length, M: traj dimension
N=size(traj,1)
# random_traj.m:9
D=size(traj,2)
# random_traj.m:10
save('original.mat','traj')
A=eye(N)
# random_traj.m:14
x=dot(eye(N - 1),- 2)
# random_traj.m:15
x=matlabarray(cat([zeros(1,N)],[x,zeros(N - 1,1)]))
# random_traj.m:16
A=A + x
# random_traj.m:17
x=eye(N - 2)
# random_traj.m:18
x=matlabarray(cat([zeros(2,N)],[x,zeros(N - 2,2)]))
# random_traj.m:19
A=A + x
# random_traj.m:20
A=matlabarray(cat([A],[zeros(1,N - 2),1,- 2],[zeros(1,N - 1),1]))
# random_traj.m:21
R_1=inv(dot(A.T,A))
# random_traj.m:22
R=dot(A.T,A)
# random_traj.m:23
y=max(R_1,[],1)
# random_traj.m:24
y=repmat(y,N,1)
# random_traj.m:25
M=dot(R_1 / y,(1 / N))
# random_traj.m:26
    ## generate traj
#### loop for each dimension, ignore the first dimension because it is the
#### time index
    for ind_D in arange(1,K,1).reshape(-1):
        theta=traj[:,2:end()]
# random_traj.m:32
        theta_k=mvnrnd(zeros(N,1),R_1,D - 1).T
# random_traj.m:33
        test_traj=theta + theta_k
# random_traj.m:34
        while DTW_dis(test_traj,theta,3) > dis_threshold:

            theta_k=dot(M,theta_k)
# random_traj.m:36
            test_traj=theta + theta_k
# random_traj.m:37

        traj_opt[ind_D]=traj + cat(zeros(N,1),theta_k)
# random_traj.m:39
    
    save('random_traj.mat','traj_opt')
    return traj_opt
    
if __name__ == '__main__':
    
    pass
    
