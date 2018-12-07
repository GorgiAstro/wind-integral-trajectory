if __name__ == "__main__":
    ## Getting Integral position
    integralSpiceId = '-198'
    observer = '500' # Earth
    from astroquery.jplhorizons import Horizons
    obj = Horizons(id=integralSpiceId,
                   location=observer,
                   epochs={'start': '2012-10-01',
                             'stop': '2012-10-02',
                             'step':'10m'},
                   id_type='id')
    vec = obj.vectors()
    # By default, coordinates should be in J2000 ecliptic coordinates, but not sure...
    integralDate_jd = [row[1] for row in vec] # Date is defined in Julian date format
    integralPosition_au = [[row[3], row[4], row[5]] for row in vec]
    au2km = 149597870.7
    integralPosition_km = [[pos[0]*au2km, pos[1]*au2km, pos[2]*au2km] for pos in integralPosition_au]
    print(integralPosition_km)
    print(integralDate_jd)

    ## Getting WIND position
    windDownloadUrl = "http://spdf.gsfc.nasa.gov/pub/data/wind/orbit/pre_or/2012/wi_or_pre_20121001_v02.cdf"
    windFileName = "wi_or_pre_20121001_v02.cdf"
    import requests
    r = requests.get(windDownloadUrl)
    with open(windFileName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=128):
            f.write(chunk)

    import cdflib
    cdfFile = cdflib.CDF(windFileName)
    windPosition_km = cdfFile.varget(variable='GSE_POS')
    # Getting position in Geocentral solar ecliptic (GSE) frame
    # Other frames are available in the CDF file:
    #   - Geocentric equatorial inertial (GCI)
    #   - Geocentric solar magnetic (GSM)
    windEpoch_PB5 = cdfFile.varget(variable='Time_PB5')
    print(windPosition_km)
    print(windEpoch_PB5)