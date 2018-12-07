if __name__ == "__main__":
    integralSpiceId = '-198'
    from astroquery.jplhorizons import Horizons
    obj = Horizons(id=integralSpiceId,
                   epochs={'start': '2012-10-01',
                             'stop': '2012-10-02',
                             'step':'10m'},
                   id_type='id')
    vec = obj.vectors()
    # By default, coordinates should be in J2000 ecliptic coordinates

    integralDate_jd = [row[1] for row in vec]
    integralPosition_au = [[row[3], row[4], row[5]] for row in vec]