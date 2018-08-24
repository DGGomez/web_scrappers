var fs = require('fs');
var nodemailer = require('nodemailer');
const {exec} = require('child_process');

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

process.on('unhandledRejection', error => {
    console.log('unhandledRejection', error);
    process.exit(1);
});

process.on('uncaughtException', error => {
  console.log('uncaughtException', error);
    process.exit(1);
});

async function Go(){
    cron.schedule('0 1 * * 1-6', function() {
        // run scripts
        exec(`python bell_bundles.py`,(err,stdout,stderr)=>{
            if(err!=null){
                console.log(err);
              }
              else{
                exec(`python compare.py`,(err,stdout,stderr)=>{
                    if(err!=null){
                        console.log(err);
                      }
                      else{
                        //if value is different
                        //send to user an email
                        nodemailer.SMTP = {
                           host: 'mail.yourmail.com',
                           port: 25,
                           use_authentication: true,
                           user: 'dggomez21@gmail.com',
                           pass: 'somepasswd'
                         };
                      
                        var message = {   
                              sender: "dggomez21@gmail.com",    
                              to:'dggomez21@gmail.com',   
                              subject: '',    
                              html: '<h1>test</h1>',  
                              attachments: [  
                              {   
                                  filename: "bell_bundles.csv",    
                                  contents: new Buffer(data, 'base64'),   
                                  cid: cid    
                              }   
                              ]   
                          };

                          nodemailer.send_mail(message,   
                            function(err) {   
                              if (!err) { 
                                  console.log('Email send ...');
                              } else console.log(sys.inspect(err));       
                          });
                      }
                });
              }
        });
    });
}

Go();
