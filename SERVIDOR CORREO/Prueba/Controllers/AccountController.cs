using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using DES.WA.REQUERIMIENTOS.BE.DTOs;

namespace FEAPIREST.Controllers
{
    [AllowAnonymous]
    public class AccountController : ApiController
    {
        /// <summary>
        /// Metodo encargado de realizar la autenticación
        /// </summary>
        /// <param name="loginDTO"></param>
        /// <returns></returns>
        [HttpPost]
        public IHttpActionResult Login(LoginDTO loginDTO)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);
            //demo
            bool iscredentialValid = (loginDTO.password == "123456");
            if (iscredentialValid)
            {
                var token = TokenGenerator.GenerateTokenJwt(loginDTO.userName);
                return Ok(token);
            }
            else
                return Unauthorized(); // status code 401

            
        }
    }
}
