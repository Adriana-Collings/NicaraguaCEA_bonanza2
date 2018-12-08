import numpy as np

np.random.seed(1)

max_age = 75.4

def lognormal(mean,sigma):
    while True:
        age = np.random.lognormal(mean=(mean), sigma=(sigma),size=None)
        if 0 <= age <= max_age:
            break
    return age

def weibull(a, lam):
    while True:
        age = np.random.weibull(a=a)
        age2 = age*lam
        if 0 <= age2 <= max_age:
            break
    return age2

def gamma(shape,rate):
    while True:
        age = np.random.gamma(shape=shape, scale=(1/rate), size=None)
        if 0 <= age <= max_age:
            break
    return age


#weibull, a = shape
# need to fix Weibull and Gamma
Age_abscess = weibull(a=1.794513, lam=35.134021)
Age_appen = lognormal(mean=3.2084729, sigma=0.4617998)
Age_finger_amp = weibull(a=1.74617, lam=34.47817)
#Age_burn = gamma(shape=0.92747608, rate = 0.0317023)
Age_csection = gamma(shape=11.6815224, rate = 0.4966885)
Age_diab = gamma(shape=17.426853, rate=0.317657)
#Age_disloc_seh = weibull(a=1.301287, lam = 24.647834)
#Age_fx_csh = lognormal(mean=2.4666958, sigma=0.7814021)
Age_hand_fx = lognormal(mean=3.0754420, sigma=0.5667893)
Age_fx_ptf = weibull(a=1.305012, lam=33.848216)
Age_ulna_radius_fx = lognormal(mean=2.272388, sigma=0.770269)
#Age_cerv_can = gamma(shape=10.1563492, rate=0.2688349)
#Age_mat_hem = lognormal(mean=3.1704848, sigma=0.4146018)
#Age_hyst = weibull(a=3.445038, lam=53.670295)
#Age_other_dis = lognormal(mean=3.0790135, sigma=0.5294391)
#Age_obstrc_lab = lognormal(mean=3.1455889, sigma=0.2260368)
#Age_cellu = gamma(shape=0.720004234, rate=0.03465062)
Age_hernia = weibull(a=1.102552, lam=26.196010)
Age_warts = lognormal(mean=2.676403, sigma=0.706539)
#Age_hypertrophy = weibull(a=9.052918, lam=69.899435)
#Age_fx_face = lognormal(mean=3.1521040, sigma=0.4868875)
#Age_fx_treated = weibull(a=1.256805, lam=25.3880747)
Age_hydrocele = lognormal(mean=3.0919091, sigma=0.5994359)
#Age_neph = weibull(a=3.50575, lam=47.92219)
Age_tumor_others = gamma(shape=3.2595522, rate = 0.1259942)
Age_biliary = lognormal(mean=3.5141305, sigma=0.3460067)
Age_ovarian = gamma(shape=9.1316594, rate = 0.2902736)
Age_phimosis = lognormal (mean=1.530508, sigma=1.141173)
Age_debrid = weibull(a=1.339371, lam=26.367772)
Age_disfig =lognormal(mean=3.5199803, sigma=0.4335448)
Age_open_wound=weibull(a=1.758986, lam=30.549057)
Age_infect = weibull(a=2.224013, lam=30.549057)
Age_breast = gamma (shape=31.546156, rate=1.183006)
Age_other_inj = weibull(a=1.499854, lam=28.900926)
#Age_paralytic_il = weibull(a=1.494522, lam=41.658403)
#Age_mat_abor = gamma(shape=17.2149750, rate=0.6221902)
#Age_blad_can = weibull(a=2.188844, lam=50.878135)
#Age_rect_fist = gamma(shape=3.6821937, rate=0.1375658)
Age_contra = gamma(shape=16.5051948, rate=0.5558921)
#Age_abdom_pelv = gamma(shape=7.127964, rate=0.225643)


#print("Abscess, weibull", Age_abscess)
#print("Appendicitis, gamma", Age_appen)
#print("Diabetes, gamma", Age_diab)
#print("Hand fx, Lognormal", Age_hand_fx)
#print("Ulna/Radius Fx, Lognormal", Age_ulna_radius_fx)
#print("Hernia, weibull", Age_hernia)
#print("Warts, lognormal",Age_warts)
#print("fx treated", Age_fx_treated)
#print("hydrocele", Age_hydrocele)
#print("tumor", Age_tumor_others)
#print("biliary", Age_biliary)
#print(Age_ovarian)
#print(Age_phimosis)
#print(Age_debrid)
#print(Age_disfig)
#print(Age_open_wound)
#print(Age_breast)
#print(Age_injury_tendon)
#print(Age_contra)