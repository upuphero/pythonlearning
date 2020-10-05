freqInMHz= 2437
signalLevelInDb




double exp = (27.55 - (20 * Math.log10(freqInMHz)) + Math.abs(signalLevelInDb)) / 20.0;
    return Math.pow(10.0, exp);
