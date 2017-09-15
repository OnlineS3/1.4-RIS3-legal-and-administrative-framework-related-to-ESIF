$(document).ready(function() {
  var auth = new auth0.WebAuth({
    domain: 'onlines3.eu.auth0.com',
    clientID: '4JrBV19wTeZ4qtNPL2nwNYttMuFWqArx'
   });


    $('.login-btn').click(function(e) {
      e.preventDefault();
      auth.authorize({
        audience: 'https://' + 'onlines3.eu.auth0.com' + '/userinfo',
        scope: 'openid profile email',
        responseType: 'code',
        redirectUri: 'http://li1088-54.members.linode.com:8082/legaladmin/callback'
      });
    });
    $('.register-btn').click(function(e) {
      e.preventDefault();
      auth.authorize({
        audience: 'https://' + 'onlines3.eu.auth0.com' + '/userinfo',
        scope: 'openid profile email',
        responseType: 'code',
        redirectUri: 'http://li1088-54.members.linode.com:8082/legaladmin/callback'
      });
    });
});

function expand(button)
{
	if(button.innerHTML == '<i class="fa fa-chevron-down fa-2x" aria-hidden="true"></i>')
	{
		button.innerHTML = '<i class="fa fa-chevron-up fa-2x" aria-hidden="true"></i>';
	}
	else
	{
		button.innerHTML = '<i class="fa fa-chevron-down fa-2x" aria-hidden="true"></i>';
	}
}