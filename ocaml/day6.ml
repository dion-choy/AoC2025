let input =
  let rows =
    String.split_on_char '\n'
      (In_channel.with_open_text "./day6.txt" In_channel.input_all)
  in
  List.take (List.length rows - 1) rows

let part1 input =
  let rec process col =
    let is_plus = List.nth col (List.length col - 1) = "+" in
    List.fold_left
      (if is_plus then ( + ) else ( * ))
      (if is_plus then 0 else 1)
      (List.map int_of_string (List.take (List.length col - 1) col))
  in
  let rec iter_col col_i all_cols =
    if col_i >= 0 then
      (all_cols
      |> List.map (List.filteri (fun i _ -> i = col_i))
      |> List.flatten |> process)
      + iter_col (col_i - 1) all_cols
    else 0
  in
  let cols_parsed =
    List.map
      (fun x ->
        List.filter (fun x -> not (x = "")) (String.split_on_char ' ' x))
      input
  in
  iter_col (List.length (List.hd cols_parsed) - 1) cols_parsed

let part2 input =
  let to_int col =
    int_of_string (String.trim (String.init (List.length col) (List.nth col)))
  in
  let rec format_col col_i all_cols =
    let col =
      all_cols |> List.map (List.filteri (fun i _ -> i = col_i)) |> List.flatten
    in
    if col_i >= 0 then
      let prev_res = format_col (col_i - 1) all_cols in
      if List.fold_left (fun acc x -> acc && x = ' ') true col then
        [] :: prev_res
      else (to_int col :: List.hd prev_res) :: List.tl prev_res
    else [ [] ]
  in
  let ops_parsed =
    List.filter
      (fun x -> not (x = ""))
      (String.split_on_char ' ' (List.nth input (List.length input - 1)))
    |> List.map (fun x -> String.get (String.trim x) 0)
  in
  let cols_parsed =
    List.take (List.length input - 1) input
    |> List.map (fun str -> List.init (String.length str) (String.get str))
  in
  List.fold_left2
    (fun acc nums op ->
      acc
      + List.fold_left
          (if op = '+' then ( + ) else ( * ))
          (if op = '+' then 0 else 1)
          nums)
    0
    (format_col (List.length (List.hd cols_parsed) - 1) cols_parsed |> List.rev)
    ops_parsed

let time f x =
  let t = Sys.time () in
  let fx = f x in
  Printf.printf "%d (%fs)\n%!" fx (Sys.time () -. t)

let () = time part1 input
let () = time part2 input
