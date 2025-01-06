function checkNumberSign(num) {
    if (num > 0) {
        console.log('რიცხვი არის დადებითი');
    } else if (num < 0) {
        console.log('რიცხვი არის უარყოფითი');
    } else {
        console.log('რიცხვი არის ნულის ტოლი');
    }
}

checkNumberSign(5);  
checkNumberSign(-3);
checkNumberSign(0);  
