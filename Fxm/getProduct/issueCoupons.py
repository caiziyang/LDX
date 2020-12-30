from Fxm.Utility.HttpRequest import HttpRequest
import requests

def issue_coupons(phone):
    url = "https://fx3t-ysqg.lhs11.com/fxc/services/ms/fxc/coupon@issueCoupons.japi"
    headers = {"cookies": 'usertoken="2uY0UF_12F_nWkiH2u_cTFibUY@@"'}
    params = {"phone": phone}

