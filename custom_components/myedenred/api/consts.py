API_BASE_URL = "https://www.myedenred.pt/edenred-customer/v2"
API_LOGIN_URL = f"{API_BASE_URL}/authenticate/default"
API_LOGIN_CHALLENGE_URL = f"{API_LOGIN_URL}/challenge"
API_LOGIN_CHALLENGE_RESEND_URL = f"{API_BASE_URL}/authenticate/challenge/resend"
API_LIST_URL = f"{API_BASE_URL}/protected/card/list"
API_ACCOUNTMOVEMENT_URL = f"{API_BASE_URL}/protected/card/{{}}/accountmovement"

API_COMMON_PARAMS = {"appVersion": "1.0", "appType": "PORTAL", "channel": "WEB"}

SESSION_PROFILE_WEB = "web"
SESSION_PROFILE_MOBILE = "android_remember_me"
# Observed in MyEdenred Portugal Android 4.2.5, EdenredBaseWebRequests.
API_MOBILE_PARAMS = {
    "appVersion": "4.2.5", "appType": "ANDROID", "channel": "MOBILE"
}
