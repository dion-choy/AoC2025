let input = String.split_on_char '\n' (String.trim (In_channel.with_open_text "./day1.txt" In_channel.input_all))

let part1 input = 
    let spin rot cur =
        let x = (cur + (if rot.[0] = 'L' then -1 else 1) * int_of_string (String.sub rot 1 (String.length rot - 1))) mod 100
        in if x >= 0 then x else 100+x
    in let rec each lst cur =
        match lst with
        | head :: tail -> let next = spin head cur
        in each tail next + if next = 0 then 1 else 0
        | [] -> 0
    in each input 50

let part2 input =
    let rec pass_zero dir rot cur =
        let next = cur + if dir = 'L' then -1 else 1
        in let next = (if next >= 0 then next else 100 + next) mod 100
        in match rot with 
        | 0 -> (cur, 0)
        | rot -> let (next, count) = pass_zero dir (rot-1) next in (next, count + if cur = 0 then 1 else 0)
    in let rec each lst cur =
        match lst with
        | head :: tail -> let (next, count) = pass_zero head.[0] (int_of_string (String.sub head 1 (String.length head - 1))) cur
        in each tail next + count
        | [] -> 0
    in each input 50

let time f x =
    let t = Sys.time() in
    let fx = f x in
    Printf.printf "%d (%fs)\n%!" fx (Sys.time() -. t)

let () = time part1 input
let () = time part2 input
