[@@@warning "-8"]
let input = List.map (fun [a; b] -> (a, b)) (
    List.map (String.split_on_char '-') (
        String.split_on_char ',' (String.trim (In_channel.with_open_text "./day2.txt" In_channel.input_all))
        (* String.split_on_char ',' (String.trim (In_channel.with_open_text "./test.txt" In_channel.input_all)) *)
        )
    )
[@@@warning "+8"]

let part1 input = 
    let check_num num_str =
        if String.length num_str mod 2 = 0 then
            if (String.sub num_str 0 (String.length num_str / 2)) = (String.sub num_str (String.length num_str / 2) (String.length num_str / 2))
            then int_of_string num_str
            else 0
        else 0
    in let rec range num target =
        if int_of_string num > int_of_string target then 0 else check_num num + range (string_of_int (int_of_string num +1)) target
    in let rec loop lst =
        match lst with
        | head :: tail -> range (fst head) (snd head) + loop tail
        | [] -> 0
    in loop input

let part2 input = 
    let rec all_equal prev lst =
        match lst with
        | first :: tail -> (first = prev) && (all_equal first tail)
        | [] -> true
    in let rec split_str num str =
        if String.length str = 0 then []
        else String.sub str 0 num :: split_str num (String.sub str num (String.length str - num))
    in let rec repeats num num_str =
        if num = String.length num_str then 0
        else 
            if String.length num_str mod num = 0 then 
                if all_equal (String.sub num_str 0 num) (split_str num num_str) then
                    int_of_string num_str
                else repeats (num+1) num_str
            else repeats (num+1) num_str
    in let rec range num target =
        if int_of_string num > int_of_string target then 0 else repeats 1 num + range (string_of_int (int_of_string num +1)) target
    in let rec loop lst =
        match lst with
        | head :: tail -> range (fst head) (snd head) + loop tail
        | [] -> 0
    in loop input

let time f x =
    let t = Sys.time() in
    let fx = f x in
    Printf.printf "%d (%fs)\n%!" fx (Sys.time() -. t)

let () = time part1 input
let () = time part2 input
