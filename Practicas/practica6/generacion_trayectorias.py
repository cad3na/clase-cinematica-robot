def trayectoria(t0, tf, q0, qf, n=100):
    from numpy import linspace
    ts = linspace(0, tf, n)
    qs = []
    q̇s = []
    q̈s = []
    # caso trivial
    if q0 == qf:
        ts = linspace(t0, tf, n)
        for t in ts:
            qs.append(q0)
            q̇s.append(0)
            q̈s.append(0)
        return ts, qs, q̇s, q̈s, 0
    # parametros comunes
    v = 3/2*(qf - q0)/(tf)
    tb = (q0 - qf + v*(tf))/v
    a = v/tb
    # se discrimina entre tiempos
    for t in ts:
        if t <= tb:
            qs.append(q0 + a/2*t**2)
            q̇s.append(a*t)
            q̈s.append(a)
        else:
            if t <= tf - tb:
                qs.append(q0 + v*(t - tb) + a/2*tb**2)
                q̇s.append(v)
                q̈s.append(0)
            else:
                if t <= tf:
                    qs.append(qf - a/2*tf**2 + a*tf*t - a/2*t**2)
                    q̇s.append(v - a*(t - tf + tb))
                    q̈s.append(-a)
    # se recalculan algunos valores para acomodar el tiempo cuando t0!=0
    ts = linspace(t0, tf, n)
    v = 3/2*(qf - q0)/(tf-t0)
    tb = t0+(q0 - qf + v*(tf-t0))/v
    return ts, qs, q̇s, q̈s, tb

def grafica_trayectoria(t0, tf, q0, qf, n=100):
    from matplotlib.pyplot import subplots, style
    style.use("ggplot")
    # se adquieren valores de funcion trayectoria
    ts, qs, q̇s, q̈s, tb = trayectoria(t0, tf, q0, qf, n)
    fig, axes = subplots(nrows=1, ncols=3, figsize=(17, 5))
    # se grafica posicion, velocidad, aceleracion
    axes[0].plot(ts, qs)
    axes[1].plot(ts, q̇s)
    axes[2].plot(ts, q̈s)
    # se calculan datos para cursores y limites
    datos = qs, q̇s, q̈s
    mins = [min(arreglo) for arreglo in datos]
    maxs = [max(arreglo) for arreglo in datos]
    spans = [ma - mi for ma, mi in zip(maxs, mins)]
    Δt = tf - t0
    for i, span in enumerate(spans):
        if span == 0:
            spans[i] = 1
    for i in range(3):
        axes[i].plot([tb, tb], [mins[i] - 0.1*spans[i], maxs[i] + 0.1*spans[i]], "--")
        axes[i].plot([tf - (tb - t0), tf - (tb - t0)], [mins[i] - 0.1*spans[i], maxs[i] + 0.1*spans[i]], "--")
        axes[i].set_xlim(-0.1*Δt + t0, 0.1*Δt + tf)
        axes[i].set_ylim(-0.1*spans[i] + mins[i], 0.1*spans[i] + maxs[i])

    return ts, qs, q̇s, q̈s