function canGiveBlood(a, b){
    if(a[a.length - 1] == "+" && b[b.length - 1] == "-"){
		return false;
	}
	else if(b[0] == "O" && a[0] != "O"){
        return false
	}
	else if((b[0] == 'B' || b[1] == 'B') && !a.includes('B')){
		return false;
	}
	else if(b[0] == "A" && !a.includes('A')){
		return false;
	}
	else{
		return true;
	}
}

console.log("(AB+ to AB+): ", canGiveBlood("AB+", "AB+"));
console.log("(A- to A+): ", canGiveBlood("A-", "A+"));
console.log("(O+ to O-): ", canGiveBlood("O+", "O-")); 