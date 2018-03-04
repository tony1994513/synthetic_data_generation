# Autogenerated with SMOP 
from smop.core import *
# 

    
@function
def random_traj(traj_dir=None,K=None,dis_threshold=None,*args,**kwargs):
    varargin = random_traj.varargin
    nargin = random_traj.nargin

    #Implemented by Ruikun Luo
#Basic idea is from STOMP paper, only generate multiple random traj
#traj = N * D, where N is the traj length, D is the traj dimension
    
    traj=Read_Traj(traj_dir)
# random_traj.m:6
    ## Precompute part
#### A, R_1, M
#### N: traj length, M: traj dimension
    N=size(traj,1)
# random_traj.m:10
    D=size(traj,2)
# random_traj.m:11
    save('original.mat','traj')
    
    A=eye(N)
# random_traj.m:15
    x=dot(eye(N - 1),- 2)
# random_traj.m:16
    x=matlabarray(cat([zeros(1,N)],[x,zeros(N - 1,1)]))
# random_traj.m:17
    A=A + x
# random_traj.m:18
    x=eye(N - 2)
# random_traj.m:19
    x=matlabarray(cat([zeros(2,N)],[x,zeros(N - 2,2)]))
# random_traj.m:20
    A=A + x
# random_traj.m:21
    A=matlabarray(cat([A],[zeros(1,N - 2),1,- 2],[zeros(1,N - 1),1]))
# random_traj.m:22
    R_1=inv(dot(A.T,A))
# random_traj.m:23
    R=dot(A.T,A)
# random_traj.m:24
    y=max(R_1,[],1)
# random_traj.m:25
    y=repmat(y,N,1)
# random_traj.m:26
    M=dot(R_1 / y,(1 / N))
# random_traj.m:27
    ## generate traj
#### loop for each dimension, ignore the first dimension because it is the
#### time index
    for ind_D in arange(1,K,1).reshape(-1):
        theta=traj[:,2:end()]
# random_traj.m:33
        theta_k=mvnrnd(zeros(N,1),R_1,D - 1).T
# random_traj.m:34
        test_traj=theta + theta_k
# random_traj.m:35
        while DTW_dis(test_traj,theta,3) > dis_threshold:

            theta_k=dot(M,theta_k)
# random_traj.m:37
            test_traj=theta + theta_k
# random_traj.m:38

        traj_opt[ind_D]=traj + cat(zeros(N,1),theta_k)
# random_traj.m:40
    
    save('random_traj.mat','traj_opt')
    return traj_opt
    
if __name__ == '__main__':
    pass