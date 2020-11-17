# sequentially
时间序列模型

1.AR,MA,ARMA,ARIMA的区别
       1.1AR模型 Auto Regressive  自回归模型 过去一段时间的点线性组合再加上白噪声预测未来某时刻的点  AR(p)
       1.2.MA 模型 Moving Average 移动平均模型 历史白噪声的线性组合影响当前时刻的点  MA(q)
        1.3.ARMA 模型 Auto Regressive Moving Average 自回归平均滑动模型  AR模型和MA模型的混合  ARMA(p,q)
         1.4.ARIMA 模型  Auto Regressive Integrated Moving Average 差分自回归平均滑动模型 ARIMA(p,d,q)   要求数据是平稳的

         预测指标AIC   AIC 越小越好
2.什么时候使用线性回归，什么时候使用时间序列分析
          对一个数值进行预测时，如果考虑的是单个时间维度与结果的关系，可以使用时间序列分析
         如果考虑的是多个变量与结果之间的关系，可以采用回归分析

3.案例学习
      3.1 比特币预测
      3.2 上证指数预测

4.依赖导出
     pip freeze >  requirements.txt 
5.依赖导入
     
