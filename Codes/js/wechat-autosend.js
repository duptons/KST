// ''
/* ! javascript
|
| Name:         wechat-autosend.js
| By:           Dupton
| Date:         2018-10-29
| Desc:			A script of auto sending WeChat message
|
| Usage:		wechat_fucker(ENV, AD, PAUSE);
| Example:		wechat_fucker('prod', "test info", 2);
| ------------------------------------------------------
*/

var ENV = 'test';
var AD = "注意 https://www.baidu.com";
var PAUSE = 3;

function wechat_fucker(ENV, AD, PAUSE){
	var chat_item = $('div[ng-repeat="chatContact in chatList track by chatContact.UserName"] > .chat_item'),
		top_chat_item = chat_item.filter('.top'),
		not_top_chat_item = chat_item.not('.top');

	ENV == 'test' && (money_items = top_chat_item);
	ENV == 'prod' && (money_items = not_top_chat_item);

	var chat_area = $('#chatArea'),
		send_area = chat_area.find('div[ng-controller=chatSenderController]'),
		Scope = send_area.scope();

	var check = function(nickname) {
		return ! (nickname.substr(0, 5) == "trans" || nickname == "文件传输助手");
	}

	var loop = function(i, T) { setTimeout(function(){
		nickname = T.find('.info > .nickname >span').text();
		if ( check(nickname) ) {
			console.log(i + ": " + nickname);
			T.click();
			Scope.editAreaCtn = AD;
			Scope.sendTextMessage();
		}
	}, i * PAUSE * 1000); }

	money_items && money_items.each(function(i){ loop(i, $(this)); });
}
