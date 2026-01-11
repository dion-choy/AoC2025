let input =
    let explode str = List.init (String.length str) (String.get str) in
    List.map (
        fun x -> List.map (fun x -> int_of_char x - int_of_char '0') (explode x))
    (String.split_on_char '\n' (String.trim (In_channel.with_open_text "./day3.txt" In_channel.input_all)))

let part1 input =
    let find_max lst = List.fold_left max 0 lst in
    let find_index_max lst = 
        Option.get (List.find_index (fun x -> x = find_max lst) lst) in
    let process lst =
        find_max (List.take (List.length lst -1) lst) * 10
        + find_max (List.drop (find_index_max (List.take (List.length lst -1) lst) +1) lst) in
    let rec loop lst =
        match lst with
        | first :: tail -> loop tail + process first
        | [] -> 0 in
    loop input

let part2 input =
    let rec exp num ex = if ex > 0 then exp num (ex-1) * num else 1 in
    let find_max lst = List.fold_left max 0 lst in
    let find_index_max lst = 
        Option.get (List.find_index (fun x -> x = find_max lst) lst) in
    let rec process cnt row =
        let sub_row = List.take ((List.length row)-cnt) row in
        if cnt >= 0 then
            process (cnt-1) (
                List.drop (find_index_max sub_row +1) row
                ) + (exp 10 cnt * find_max sub_row)
        else 0 in
    let rec loop lst =
        match lst with
        | first :: tail -> loop tail + process 11 first
        | [] -> 0 in
    loop input

let time f x =
    let t = Sys.time() in
    let fx = f x in
    Printf.printf "%d (%fs)\n%!" fx (Sys.time() -. t)

let () = time part1 input
let () = time part2 input
