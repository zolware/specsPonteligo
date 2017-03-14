# Note: 
# when executed in the build dir, CMAKE_CURRENT_SOURCE_DIR is the build dir.
file( COPY images snippets tests DESTINATION "${CMAKE_ARGV3}" )
file( COPY doc  DESTINATION "${CMAKE_ARGV3}" )
#FILES_MATCHING PATTERN "*.py" PATTERN "*.rst" PATTERN "*.html" PATTERN "*.css")
