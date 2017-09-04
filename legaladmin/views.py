from django.shortcuts import render,redirect
import json
from auth0.v3.authentication import GetToken
from auth0.v3.authentication import Users

client_id = "4JrBV19wTeZ4qtNPL2nwNYttMuFWqArx"
client_secret = "u0YGFqhyJvOn9zb_xnLbTem3heqx8lkaiom7Q2xvFX9uVV7ajhRVjRuG3BYNW0T7"

def index(request):
	return render(request, 'legaladmin/index.html')

def guide(request):
	return render(request, 'legaladmin/guide.html')

def about(request):
	return render(request, 'legaladmin/about.html')

def access(request):
	return render(request, 'legaladmin/access_app.html')

def related(request):
	return render(request, 'legaladmin/related_documents.html')

def callback(request):
	code = request.GET['code']
	get_token = GetToken('onlines3.eu.auth0.com')
	auth0_users = Users('onlines3.eu.auth0.com')
	token = get_token.authorization_code(client_id, client_secret, code, 'http://li1088-54.members.linode.com:8082/legaladmin/callback/')
	user_info = auth0_users.userinfo(token['access_token'])
	request.session['legaladmin_profile'] = json.loads(user_info)
	#save user to db and session
	return redirect('legaladmin_index')

def logout(request):
	request.session['legaladmin_profile'] = None
	#parsed_base_url = urlparse('http://li1088-54.members.linode.com:8082/bscapp/callback/')
	#base_url = parsed_base_url.scheme + '://' + parsed_base_url.netloc
	#return redirect('https://%s/v2/logout?returnTo=%s&client_id=%s' % ('onlines3.eu.auth0.com', base_url, 'vE0hJ4Gx1uYG9LBtuxgqY7CTIFmKivFH'))
	return redirect('legaladmin_index')
