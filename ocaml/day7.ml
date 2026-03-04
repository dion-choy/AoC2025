let input =
  String.split_on_char '\n'
    (String.trim (In_channel.with_open_text "./day7.txt" In_channel.input_all))

let part1 input =
  let rec split_i prev row (accum, cnt) =
    match prev with
    | head :: tail ->
        let is_splitter = String.get row head = '^' in
        split_i tail row
          ( (if is_splitter then (head - 1) :: (head + 1) :: accum
             else head :: accum),
            if is_splitter then cnt + 1 else cnt )
    | [] -> (accum, cnt)
  in
  Pair.snd
    (List.fold_left
       (fun acc row ->
         let next, cnt = split_i (Pair.fst acc) row ([], Pair.snd acc) in
         (List.sort_uniq compare next, cnt))
       ([ String.index (List.hd input) 'S' ], 0)
       (input
       |> List.filter (fun x ->
           x <> String.init (String.length (List.hd input)) (Fun.const '.'))))

let part2 input =
  let rec combine lst =
    match lst with
    | head :: tail ->
        let combined = combine tail in
        let k, v = head in
        if List.mem_assoc k combined then
          (k, v + List.assoc k combined) :: List.remove_assoc k combined
        else head :: combined
    | [] -> []
  in
  let rec split_i prev row =
    match prev with
    | head :: tail ->
        let k, v = head in
        (if String.get row k = '^' then [ (k - 1, v); (k + 1, v) ] else [ head ])
        @ split_i tail row
    | [] -> []
  in
  List.fold_left
    (fun acc (k, v) -> v + acc)
    0
    (List.fold_left
       (fun acc row -> split_i acc row |> combine)
       [ (String.index (List.hd input) 'S', 1) ]
       (input
       |> List.filter (fun x ->
           x <> String.init (String.length (List.hd input)) (Fun.const '.'))))

let time f x =
  let t = Sys.time () in
  let fx = f x in
  Printf.printf "%d (%fs)\n%!" fx (Sys.time () -. t)

let () = time part1 input
let () = time part2 input
