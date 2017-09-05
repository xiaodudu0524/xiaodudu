$(function(){

	var error_name = true;
	var error_password = true;
	var error_check_password = true;
	var error_email = true;
	var error_check = false;
	var error_check_phone = false


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});
	$('#phone').blur(function () {
		check_phone();
    })
	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});

	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名');
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
            $.get('/user/register_exist/?uname='+$('#user_name').val(),function (data) {
				if(data.count==1){
					$('#user_name').next().html('用户名已经存在').show();
					error_name = true;
				}else{
					$('#user_name').next().hide();
                	error_name = false;
				}
            });
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}

	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('您输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}

	function check_phone(){
		var len = $('#phone').val().length
		if(len!=11){
			$('#phone').next().html('您输入的手机号码格式不正确')
			$('#phone').next().show()
			error_check_phone = true;
		}else{
			$('#phone').next().hide()
			error_check_phone = false;
		}
	}

	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();
		check_phone();
		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false && error_check_phone == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});

})