enum exercise = {A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, cooldown};
array[exercise, feature] of int: info = [|A1, 5, light|A2, 10, light|A3, 8, light|A4, 15, heavy|A5, 6, light|A6, 20, heavy|A7, 10, light|A8, 5, light|A9, 21, heavy|A10, 9, light|cooldown, 0, light|];
int: slot = 5;
int: min_calorie = 308;
enum feature = {name, calorie, types};
enum e_type = {light, heavy};
int: max_calorie = min_calorie + 50;
int: min_time ;
int: max_time = 20;
%int: min_duration = 60;
%int: max_duration = min_duration + 10;
array[1..7,1..slot] of var exercise: roster;
array[1..7,1..slot] of var int: time;
%array[1..7,1..slot] of var e_type: box;
%array[1..slot] of var int: time;
%constraint forall(i in 1..7,j in 1..slot)(box[i,j] = info[roster[i,j],types]);
constraint forall(i in 1..7) (info[roster[i,1],types] = light /\ roster[i,slot] = cooldown);
constraint forall(i in 1..7-1,j in 1..slot)(info[roster[i,j],types] = heavy -> forall(l in 1..slot)(info[roster[i+1,l],types] != heavy));
constraint forall(i in exercise) (sum(j in 1..7,k in 1..slot)(roster[j,k] = i) >= 1);
constraint exists(m in exercise)(info[m,types] = heavy) -> sum(i in 1..7, j in 1..slot)(info[roster[i,j],types] = heavy) == 4;
constraint forall(i in 1..7,j in 1..slot-1)(info[roster[i,j],types] = heavy ->forall(k in j+1..slot-1)(info[roster[i,k],types] != heavy));
constraint forall(i in 1..7,j in 1..slot-1)(forall(k in j+1..slot-1)(roster[i,j] !=roster[i,k]));
constraint forall(i in 1..7-1,j in 1..slot-2)(roster[i,j] !=roster[i+1,j]);
%constraint forall(i in 1..7,j in 1..slot-1)(roster[i,j] !=roster[i,j+1]);
constraint forall(i in 1..7,j in 1..slot-1) (roster[i,j] != cooldown);

constraint forall(i in 1..7,j in 1..slot) (time[i,j] > 0);
%constraint sum(i in 1..slot) (time[i]) >= min_duration;
%constraint sum(i in 1..slot) (time[i]) <= max_duration;
constraint forall(i in 1..7)(sum(j in 1..slot)(info[roster[i,j],calorie] * time[i,j])>= min_calorie) ;
constraint forall(i in 1..7)(sum(j in 1..slot)(info[roster[i,j],calorie] * time[i,j])<= max_calorie) ;
constraint forall(i in 1..7,j in 1..slot) (time[i,j] >= min_time);
constraint forall(i in 1..7,j in 1..slot) (time[i,j] <= max_time);
constraint forall(i in 1..7,j in 1..slot-1)(forall(k in j+1..slot)(time[i,j] !=time[i,k]));
constraint forall(i in 1..7-1,j in 1..slot-1)(time[i,j] != time[i+1,j]);

constraint forall(i in 1..7) (time[i,slot] = 10);
%constraint forall(i in ) ()
%constraint forall(i in 1..length(exercise))(exists(j in 1..days,k in 1..slot)(roster[j,k] = exercise[i]));
%output["\(roster)\n"]%++["\(to_enum(e_type,info[roster[i],types])) "|i in 1..slot];

%constraint forall(i in exercise)(count(roster,i)>=1);
solve satisfy;
%output["\(roster[i,j]) \(time[i,j])"|i in 1..7,j in 1..slot];
output[if k = 1 then "\n" else " " endif ++
      "\(roster[i,k]) \(time[i,k])"
   | i in 1..7, k in 1..slot]; %++[if k = 1 then "\n" else " " endif ++
  %     show(box[i,k])
  %  | i in 1..7, k in 1..slot]++["\n"] ++ [if k = 1 then "\n" else " " endif ++
  %     show(time[i,k])
  %  | i in 1..7, k in 1..slot] ;
