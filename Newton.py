def Newton(f,x,dfdx, epsilon=1.07E-7,N=100,store=False):
    f_value = f(x)
    n = 0
    if store: info = [(x,f_value)]
    while abs(f_value) > epsilon and n <= N:
        dfdx_value = float(dfdx(x))
        if abs(dfdx_value) < 1E-14:
            raise ValueError("Newton: f'(%g)=%g" %(x, dfdx_value))
        x = x - (f_value/dfdx_value)
        n +=1
        f_value = f(x)
        if store: info.append((x,f_value))
    if store:
        return x, info 
    else:
        return x, n, f_value
        

