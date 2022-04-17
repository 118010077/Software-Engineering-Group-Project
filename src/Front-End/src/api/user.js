import request from '@/utils/request'

export function login(loginForm) {
  return request({
    url: '/api/login',
    method: 'post',
    data: {
      userEmail: loginForm.email.trim(),
      password: loginForm.password
    }
  })
}

export function register(registerForm) {
  return request({
    url: '/api/register',
    method: 'post',
    data: {
      userName: registerForm.name,
      userEmail: registerForm.email,
      password: registerForm.password
    }
  })
}

export function sendVerification(emial) {
  return request({
    url: '/api/sendverification',
    methond: 'post',
    data: { email }
  })
}

export function getInfo(token) {
  return request({
    url: '/api/getprofile',
    method: 'post',
    params: { token }
  })
}

