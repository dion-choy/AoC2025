let input =
  String.split_on_char '\n'
    (In_channel.with_open_text "./day5.txt" In_channel.input_all)

let ranges =
  input
  |> List.filter (fun x -> String.contains x '-')
  |> List.map (fun x ->
      match String.split_on_char '-' x with
      | [ a; b ] -> (int_of_string a, int_of_string b)
      | _ -> failwith "Invalid input format")

let fruits =
  input
  |> List.filter (fun x ->
      List.fold_left
        (fun acc y -> acc || String.contains x y)
        false
        (List.init 10 (fun x -> char_of_int (x + int_of_char '0')))
      && not (String.contains x '-'))
  |> List.map int_of_string

let part1 fruits ranges =
  List.fold_left
    (fun acc x ->
      acc
      +
      if
        List.fold_left
          (fun acc (rng_start, rng_end) ->
            acc || (x >= rng_start && x <= rng_end))
          false ranges
      then 1
      else 0)
    0 fruits

let part2 ranges =
  (ranges
  |> List.sort (fun (a_start, a_end) (b_start, b_end) -> a_start - b_start)
  |> List.fold_left
       (fun acc (rng_start, rng_end) ->
         let last_start, last_end = List.hd acc in
         if rng_start > last_end then [ (rng_start, rng_end) ] @ acc
         else
           [
             ( List.fold_left min Int.max_int
                 [ rng_start; rng_end; last_start; last_end ],
               List.fold_left max 0 [ rng_start; rng_end; last_start; last_end ]
             );
           ]
           @ List.drop 1 acc)
       [ (0, 0) ]
  |> List.fold_left
       (fun acc (rng_start, rng_end) -> rng_end - rng_start + 1 + acc)
       0)
  - 1

let time f x =
  let t = Sys.time () in
  let fx = f x in
  Printf.printf "%d (%fs)\n%!" fx (Sys.time () -. t)

let time2 f x y =
  let t = Sys.time () in
  let fx = f x y in
  Printf.printf "%d (%fs)\n%!" fx (Sys.time () -. t)

let () = time2 part1 fruits ranges
let () = time part2 ranges
