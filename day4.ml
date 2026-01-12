let input =
  let explode str = List.init (String.length str) (String.get str) in
  List.map explode
    (String.split_on_char '\n'
       (String.trim
          (In_channel.with_open_text "./day4.txt" In_channel.input_all)))

(* let () = List.iter (fun x -> List.iter (Printf.printf "%c, ") x; print_endline "") input *)

let part1 input =
  let padding grid =
    [ List.init (List.length grid + 2) (fun x -> '.') ]
    @ List.map (fun x -> [ '.' ] @ x @ [ '.' ]) grid
    @ [ List.init (List.length grid + 2) (fun x -> '.') ]
  in
  let process three_row =
    let rec scan_window count lst =
      match lst with
      | a :: b :: c :: tail ->
          let window3x3 =
            three_row |> List.map (fun x -> x |> List.drop count |> List.take 3)
          in
          scan_window (count + 1) ([ b; c ] @ tail)
          +
          if List.nth (List.nth window3x3 1) 1 = '@' then
            if
              (window3x3
              |> List.fold_left
                   (fun acc x ->
                     acc + (x |> List.filter (fun x -> x = '@') |> List.length))
                   0)
              - 1
              < 4
            then 1
            else 0
          else 0
      | _ -> 0
    in

    scan_window 0 (List.hd three_row)
  in
  let rec get_cnt lst =
    match lst with
    | a :: b :: c :: tail -> get_cnt ([ b; c ] @ tail) + process [ a; b; c ]
    | _ -> 0
  in
  input |> padding |> get_cnt

let part2 input =
  let padding grid =
    [ List.init (List.length grid + 2) (fun x -> '.') ]
    @ List.map (fun x -> [ '.' ] @ x @ [ '.' ]) grid
    @ [ List.init (List.length grid + 2) (fun x -> '.') ]
  in
  let process three_row =
    let rec scan_window count lst =
      match lst with
      | a :: b :: c :: tail ->
          let window3x3 =
            three_row |> List.map (fun x -> x |> List.drop count |> List.take 3)
          in
          let center = List.nth (List.nth window3x3 1) 1 in
          let access =
            center = '@'
            && (window3x3
               |> List.fold_left
                    (fun acc x ->
                      acc + (x |> List.filter (fun x -> x = '@') |> List.length))
                    0)
               - 1
               < 4
          in
          let cnt, row = scan_window (count + 1) ([ b; c ] @ tail) in
          ( (cnt + if access then 1 else 0),
            [ (if access then '.' else center) ] @ row )
      | _ -> (0, [])
    in
    scan_window 0 (List.hd three_row)
  in
  let rec get_cnt lst =
    match lst with
    | a :: b :: c :: tail ->
        let row_cnt, row = process [ a; b; c ] in
        let total_cnt, prev_rows = get_cnt ([ b; c ] @ tail) in
        (row_cnt + total_cnt, [ row ] @ prev_rows)
    | _ -> (0, [])
  in
  let rec repeat grid =
    let cnt, next_grid = grid |> padding |> get_cnt in
    if cnt <> 0 then cnt + repeat next_grid else 0
  in
  repeat input

let time f x =
  let t = Sys.time () in
  let fx = f x in
  Printf.printf "%d (%fs)\n%!" fx (Sys.time () -. t)

let () = time part1 input
let () = time part2 input
