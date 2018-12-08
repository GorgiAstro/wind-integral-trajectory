if __name__ == "__main__":
    ## Parameters
    from datetime import datetime, timezone
    startDate = datetime(2012, 10, 1, tzinfo=timezone.utc)
    endDate = datetime(2012, 11, 15, tzinfo=timezone.utc)

    ## Getting Integral position
    integralSpiceId = '-198'
    observer = '500' # Earth
    from astroquery.jplhorizons import Horizons
    epochs = {'start': '{:4d}-{:02d}-{:02d}'.format(startDate.year, startDate.month, startDate.day),
                             'stop': '{:4d}-{:02d}-{:02d}'.format(endDate.year, endDate.month, endDate.day),
                             'step': '10m'}
    obj = Horizons(id=integralSpiceId,
                   location=observer,
                   epochs=epochs,
                   id_type='id')
    vec = obj.vectors()
    # By default, coordinates should be in J2000 ecliptic coordinates, but not sure...
    import numpy as np
    integralDate_jd = np.array([row[1] for row in vec]) # Date is defined in Julian date format
    integralPosition_au = np.array([[row[3], row[4], row[5]] for row in vec])
    au2km = 149597870.7
    integralPosition_km = au2km * integralPosition_au
    #print(integralPosition_km)
    #print(integralDate_jd)

    ## Getting WIND position
    import cdflib
    from pathlib import Path
    windPosition_km = None
    windEpoch_PB5 = None
    p = Path('.')
    for windFileName in sorted(p.glob('../../pre_or/*/*.cdf')):
        fileNameWithoutPath = windFileName.name
        fileYear = int(fileNameWithoutPath[10:14])
        fileMonth = int(fileNameWithoutPath[14:16])
        fileDay = int(fileNameWithoutPath[16:18])
        fileDate = datetime(fileYear, fileMonth, fileDay, tzinfo=timezone.utc)
        if (fileDate >= startDate) and (fileDate <= endDate):
            print(fileDate)
            cdfFile = cdflib.CDF(windFileName)
            if windPosition_km is None:
                windPosition_km = cdfFile.varget(variable='GCI_POS')
                windEpoch_PB5 = cdfFile.varget(variable='Time_PB5')
            else:
                windPosition_km = np.concatenate((windPosition_km, cdfFile.varget(variable='GCI_POS')))
                # Getting position in Geocentral solar ecliptic (GSE) frame
                # Other frames are available in the CDF file:
                #   - Geocentric equatorial inertial (GCI)
                #   - Geocentric solar magnetic (GSM)
                windEpoch_PB5 = np.concatenate((windEpoch_PB5, cdfFile.varget(variable='Time_PB5')))

    #print(windPosition_km)
    #print(windEpoch_PB5)

    ## Writing Earth shape for plotting
    R_earth_km = 6371.0
    x_earth_km = np.array([R_earth_km * np.cos(t) for t in np.linspace(0, 2*np.pi, 100)])
    y_earth_km = np.array([R_earth_km * np.sin(t) for t in np.linspace(0, 2*np.pi, 100)])

    ## Plotting
    import matplotlib.pyplot as plt
    plt.plot(x_earth_km, y_earth_km, 'k')
    plt.plot(0.0, 0.0, 'k', marker='x', label='Earth')
    plt.plot(windPosition_km[:, 0], windPosition_km[:, 1], 'C0', label='WIND',)
    plt.plot(windPosition_km[-1, 0], windPosition_km[-1, 1], 'C0', marker='.', markersize=10)
    plt.plot(integralPosition_km[:, 0], integralPosition_km[:, 1], 'C1', label='Integral')
    plt.plot(integralPosition_km[-1, 0], integralPosition_km[-1, 1], 'C1', marker='.', markersize=10)
    plt.xlabel('X (km)')
    plt.ylabel('Y (km)')
    plt.title('Integral and WIND trajectory around the Earth, Earth-centered inertial coordinates in ecliptic plane')
    plt.axis('equal')
    plt.legend()
    plt.show()