<!DOCTYPE html>
<html>
<head>
	<title>verk-4</title>
	<link rel="stylesheet" type="text/css" href="/static/main.css">
</head>
<body>
	<header><h1>Nemendur:</h1></header>
	<section>
		<table>
			<tbody>
				<tr>
					<th>Kennitala</th>
					<th>Nöfn</th>
					<th>Braut</th>
				</tr>
				%for nemandi in bekkur['nemendur']:
					<tr>
						<td><a href="/nemandi/{{nemandi['kt']}}">{{nemandi['kt']}}</a></td>
						<td>{{nemandi['nafn']}}</td>
						<td>{{nemandi['braut']}}</td>
					</tr>
				% end
			</tbody>
		</table>
	</section>
	<footer><h6>verkefni 4 - Vefforritun - Róbert Ingi Hálfdanarson</h6></footer>
</body>
</html>