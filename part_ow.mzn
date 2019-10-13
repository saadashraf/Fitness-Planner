enum feature = {name, calorie, types};
enum e_type = {light, heavy};
int: max_calorie = min_calorie + 50;
int: min_time ;
int: max_time = 20;

array[1..7,1..slot] of var exercise: roster;
array[1..7,1..slot] of var int: time;

% ensures that the last exercise is cooldown
constraint forall(i in 1..7) (info[roster[i,1],types] = light /\ roster[i,slot] = cooldown);

%ensure only one heavy exercise is present between two consecutive days
constraint forall(i in 1..7-1,j in 1..slot)(info[roster[i,j],types] = heavy -> forall(l in 1..slot)(info[roster[i+1,l],types] != heavy));

% ensures every exercise is present atleast once
constraint forall(i in exercise) (sum(j in 1..7,k in 1..slot)(roster[j,k] = i) >= 1);

%ensures heavy evercise are present on aternating days
constraint exists(m in exercise)(info[m,types] = heavy) -> sum(i in 1..7, j in 1..slot)(info[roster[i,j],types] = heavy) == 4;

%introduce randomization so that person does not do same type at the same time
constraint forall(i in 1..7,j in 1..slot-1)(info[roster[i,j],types] = heavy ->forall(k in j+1..slot-1)(info[roster[i,k],types] != heavy));

%ensures exercise are not the same horizontally
constraint forall(i in 1..7,j in 1..slot-1)(forall(k in j+1..slot-1)(roster[i,j] !=roster[i,k]));

%ensures exercise are not the same vertically
constraint forall(i in 1..7-1,j in 1..slot-2)(roster[i,j] !=roster[i+1,j]);

% ensures all the other exercise except the last one is not cooldown
constraint forall(i in 1..7,j in 1..slot-1) (roster[i,j] != cooldown);

%ensure that all the exercises are allotted some time
constraint forall(i in 1..7,j in 1..slot) (time[i,j] > 0);



% checks the calorie burn is within range
constraint forall(i in 1..7)(sum(j in 1..slot)(info[roster[i,j],calorie] * time[i,j])>= min_calorie) ;
constraint forall(i in 1..7)(sum(j in 1..slot)(info[roster[i,j],calorie] * time[i,j])<= max_calorie) ;

% checks the total time spent is within the range
constraint forall(i in 1..7,j in 1..slot) (time[i,j] >= min_time);
constraint forall(i in 1..7,j in 1..slot) (time[i,j] <= max_time);

%ensure that time are not alloted equally
constraint forall(i in 1..7,j in 1..slot-1)(forall(k in j+1..slot)(time[i,j] !=time[i,k]));
constraint forall(i in 1..7-1,j in 1..slot-1)(time[i,j] != time[i+1,j]);

% set cooldowndown time to 10 min
constraint forall(i in 1..7) (time[i,slot] = 10);
 
 
 

%minimizing time to get better output, but it takes a lot of time, so we used satisfy
%solve minimize sum(i in 1..7,j in 1..slot) (time[i,j]);
solve satisfy;

output[if k = 1 then "\n" else " " endif ++
      "\(roster[i,k]) \(time[i,k])"
   | i in 1..7, k in 1..slot]; 
 