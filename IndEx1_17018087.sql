/*
Write SQL queries that can be executed on the chinook.sqlite database to provide answers the following questions.
Save your SQL to this .sql file. Do not include the query results.
In PyCharm you can right click on the file name in the Project pane and select Refactor > Rename, and replace STU_NUM with your student number.
*/

--1. Which employees have 'IT' in their job title? (list their EmployeeId, FirstName, LastName and Title)
SELECT EmployeeID, FirstName, LastName, Title
from Employee
WHERE
Title LIKE '%IT%';

--2. List the names of all Artists and the titles of their albums
SELECT Name, Title
from Artist
    JOIN Album ON Artist.ArtistId = Album.ArtistId;

--3. Which track(s) features the greatest number of times in playlists and how many times is it/are they included? (list Track name and the total number of appearances in playlists).
SELECT Track.Name, count(*) AS Count
from Track
    JOIN PlaylistTrack PT on Track.TrackId = PT.TrackId
GROUP BY Track.TrackId
ORDER BY Count DESC;

--4. Provide a list of the number of tracks by each artist
SELECT Artist.Name AS ArtistName, COUNT(Album.Title) AS NoOfTracks
from Track
    JOIN Album on Track.AlbumId = Album.AlbumId
    JOIN Artist on Album.ArtistId = Artist.ArtistId
GROUP BY Artist.Name
ORDER BY NoOfTracks DESC;

--5. How much money has been invoiced for the artist Deep Purple? (For this you can create two queries, one that shows the line item from the invoices and the total amount per line, and another that sums the totals from each line)
SELECT InvoiceLineId, InvoiceLine.TrackId, InvoiceLine.InvoiceId, Quantity * InvoiceLine.UnitPrice AS LineTotal
FROM Artist
    JOIN InvoiceLine
    JOIN Track T on InvoiceLine.TrackId = T.TrackId
    JOIN Invoice I on InvoiceLine.InvoiceId = I.InvoiceId
WHERE ArtistId=58;

SELECT Artist.Name as Artist_Name, SUM(Quantity * InvoiceLine.UnitPrice) AS TotalSum
FROM Artist
    JOIN InvoiceLine
    JOIN Track T on InvoiceLine.TrackId = T.TrackId
    JOIN Invoice I on InvoiceLine.InvoiceId = I.InvoiceId
WHERE ArtistId=58;

